#!/usr/bin/env python3
import json
import requests

from time import sleep
from getpass import getpass
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler


API = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
DEBUG = False

country = input('What country would you like to monitor? #> ')
city = input('What city would you like to additionally monitor? #> ')

if not DEBUG:
	TOKEN = getpass('Enter Telegram API key (hidden): ')
	CHAT_ID = getpass('Enter Telegram Chat-Id (hidden): ')
	TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="

cache = []
alerted = []


def get_loc(quake):
	try:
		return quake['properties']['place'].lower()
	except:
		return None


def telegram_notify(quake):
	global TELEGRAM_URL, DEBUG
	time = datetime.now().strftime('%Y-%m-%d')
	magnitude = quake['properties']['mag']
	place = get_loc(quake)
	msg = f'[ALERT] {time} Earthquake of magnitude {magnitude} occurred {place}!'
	r =	requests.get(f'{TELEGRAM_URL}{msg}')


def check_cache(quake):
	global alerted
	loc = get_loc(quake)
	mag = quake['properties']['mag']
	cached = f'{loc} {mag}'
	if cached in alerted:
		return True
	alerted.append(cached)
	return False


def check_loc_and_notify(c, cc):
	global cache
	for quake in cache:
		loc = get_loc(quake)
		ct = c.lower() in loc
		cct = cc.lower() in loc
		if (ct or cct) and not check_cache(quake):
			telegram_notify(quake)


def get_data(c, cc):
	global API, cache
	r = requests.get(API)
	js = r.json()
	lst = js['features']
	if cache != lst:
		cache = lst
	check_loc_and_notify(c, cc)


def clear_cache():
	global cache, alerted
	alerted = []
	cache = []


def loop():
	global country, city
	get_data(country, city)


if __name__ == '__main__':
	if DEBUG:
		loop()
		exit(0)
	scheduler = BlockingScheduler()
	scheduler.add_job(clear_cache, 'cron', day=3, hour=0, minute=0, second=15)
	scheduler.add_job(loop, 'interval', seconds=30)
	try:
		cache = requests.get(API).json()['features']
		cty = cache[0]['properties']['place'].split(',')[-1].strip()
		msg = f'[INFO] Scheduler initialised and listening for country: {country} and city {city}. Executing test-run using {cty}...'
		r = requests.get(f'{TELEGRAM_URL}{msg}')
		print(f'[INFO] Executing test run with city {cty}...')
		get_data(cty, cty)
		print('[INFO] Test run complete. Starting scheduler...')
		scheduler.start()
	except KeyboardInterrupt:
		pass
