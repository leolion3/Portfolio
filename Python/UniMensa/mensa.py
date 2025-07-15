#!/usr/bin/env python3
import requests
import re
import json
import getpass
import urllib
from typing import List, Dict
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


DEBUG = False

message_template = """
Das heutige Mensa-Essensangebot ([DATE]):

"""
food_template = "- [FOOD]: [PRICE]\n"

if not DEBUG:
	TOKEN = getpass.getpass('Enter Telegram API Key:')
	CHAT_ID = getpass.getpass('Enter Telegram Chat ID:')
	TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="

url = 'https://www.stw-bremen.de/de/essen-und-trinken/universitaet-bremen/uni-mensa/'
api_url: str = 'https://content.stw-bremen.de/api/kqlnocache'
payload: Dict[str, str] = {
"query":f"page('meals').children.filterBy('location', '300').filterBy('date', '{datetime.now().strftime('%Y-%m-%d')}').filterBy('printonly', 0)",
"select": {
		"title": True,
		"ingredients":"page.ingredients.toObject",
		"prices":"page.prices.toObject",
		"location": True,
		"counter": True,
		"date": True,
		"mealadds": True,
		"mark": True,
		"frei3": True,
		"printonly": True,
		"kombicategory": True,
		"categories":"page.categories.split"
	}
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0',
	'X-Language': 'de'
}

def get_todays_food() -> str:
	global url, api_url, payload, headers
	s = requests.session()
	s.get(url, headers=headers)
	r = s.post(api_url, headers=headers, json=payload)
	return r.json()


def get_foods(today: Dict[str, str]) -> List[str]:
	try:
		return [f['title'] for f in today['result']]
	except:
		return []


def get_prices(today: str) -> List[str]:
	try:
		foods = today['result']
		prices: List[List[Dict[str, str]]] = [f['prices'] for f in foods]
		actual = []
		for price_list in prices:
			for price in price_list:
				if 'stud' in price['label'].lower():
					actual.append(price['price'].strip() + '€')
					break
		return actual
	except Exception as e:
		print(e)
		return []


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
