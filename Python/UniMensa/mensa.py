#!/usr/bin/env python3
import requests
import re
import json
import getpass
import urllib
from typing import List
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


DEBUG = False

food_splitter = 'food-plan-header'
name_splitter = 'field-name-field-description">'
student_price_splitter = 'field-name-field-price-students">'
closing_tag_split = '</td>'
message_template = """
Das heutige Mensa-Essensangebot ([DATE]):

"""
food_template = "- [FOOD]: [PRICE]\n"

if not DEBUG:
	TOKEN = getpass.getpass('Enter Telegram API Key:')
	CHAT_ID = getpass.getpass('Enter Telegram Chat ID:')
	TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="


def get_todays_food() -> str:
	global food_splitter
	url = 'https://www.stw-bremen.de'
	r = requests.get(url)
	# Index 1 entry is always current day
	return r.text.split(food_splitter)[1]


def clean_up_food_name(name: str) -> str:
	if '<sup>' in name:
		name = re.sub("<sup>(.+?)</sup>", '', name)
	return name.replace('\r\n', ' ').replace('  ', ' ')


def get_foods(today: str) -> List[str]:
	global name_splitter, closing_tag_split
	foods = []

	for food in today.split(name_splitter)[1:]:
		name = food.split(closing_tag_split)[0]
		name = clean_up_food_name(name) 	
		if not 'wechselndes' in name:
			# No price or details for sauces
			foods.append(name)
	return foods


def get_prices(today: str) -> List[str]:
	global student_price_splitter, closing_tag_split
	prices = []
	for student_price in today.split(student_price_splitter)[1:]:
		price = student_price.split(closing_tag_split)[0]
		prices.append(price)
	return prices


def pretty_print(foods: List[str], prices: List[str]) -> str:
	global message_template, food_template
	output = message_template.replace('[DATE]', datetime.now().strftime('%d/%m/%y'))
	for i, f in enumerate(foods):
		if len(foods) != len(prices):
			output += food_template.replace('[FOOD]', f).replace(': [PRICE]', '')
			continue
		output += food_template.replace('[FOOD]', f).replace('[PRICE]', prices[i])
	return output


def send_telegram_message(message: str) -> None:
	global DEBUG
	if DEBUG:
		print('Running in debug, telegram unavailable!')
		print(message)
		return
	global TELEGRAM_URL
	r = requests.get(f'{TELEGRAM_URL}{message}')
	if r.status_code != 200:
		print('Error during request. Trace: ', r.text)
	else:
		print(message)


def schedule():
	html = get_todays_food()
	f = get_foods(html)
	p = get_prices(html)
	# Weekends
	if not len(f):
		if datetime.today().weekday() > 4:
			return
		# Holidays, etc
		send_telegram_message('No mensa food available today!')
		return
	pp = pretty_print(f, p)
	send_telegram_message(urllib.parse.quote(pp))


if __name__ == '__main__':
	if DEBUG:
		schedule()
		exit()
	scheduler = BlockingScheduler()
	scheduler.add_job(schedule, 'cron', day=1, hour=11, minute=0)
	try:
		r = requests.get(f'{TELEGRAM_URL}Mensa food listener up and running!')
		if r.status_code != 200:
			print('Error connecting to Telegram, please check your configs!')
			print(r.text)
			exit(-1)
		print('Executing test run...')
		schedule()
		scheduler.start()
	except Exception as e:
		print(e)
		pass
