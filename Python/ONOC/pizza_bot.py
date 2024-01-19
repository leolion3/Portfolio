#!/usr/bin/env python3
import requests
import getpass
from apscheduler.schedulers.blocking import BlockingScheduler


URL = 'https://onoc.eu/app/pizza/orders/ready-to-collect'
TELEGRAM_API_KEY = getpass.getpass('Telegram API Key (Redacted): ')
TELEGRAM_CHAT_ID = getpass.getpass('Telegram Chat ID (Redacted): ')
if not TELEGRAM_API_KEY or not TELEGRAM_CHAT_ID:
	print('Telegram credentials missing, terminating...')
	exit(-1)

TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text='

# Pizzas to await
watched = [154, 134]
# Received pizzas
found = []


def query():
	r = requests.get(URL)
	if r.status_code == 200:
		return r.json()
	return []


def watchdog():
	pizzas = query()
	print('Retrieved pizzas:', pizzas, end='\r')
	for pizza in pizzas:
		if pizza in watched and pizza not in found:
			message = f'[BOT] Pizza {pizza} is ready to collect.'
			r = requests.get(TELEGRAM_URL + message)
			if r.status_code == 200:
				found.append(pizza)
	if len(watched) == len(found):
		print('[BOT] All pizzas delivered, terminating...')
		scheduler.shutdown()


if __name__ == '__main__':
	scheduler = BlockingScheduler()
	scheduler.add_job(watchdog, 'interval', seconds=15)
	try:
		test_message = TELEGRAM_URL + '[BOT] Listening for pizzas...'
		requests.get(test_message)
		scheduler.start()
	except KeyboardInterrupt:
		print("Scheduler stopped, terminating...")