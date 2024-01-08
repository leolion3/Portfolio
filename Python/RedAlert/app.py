#!/usr/bin/env python3
# Red alert endpoint functionality reverse engineered from https://github.com/Zontex/python-red-alert
# NOTE: This app can only be ran from Israel or using Israeli VPN, as red alert 
import requests
import json
import os
import subprocess
import logging
logging.basicConfig(filename='file.log',level=logging.DEBUG)

from logging import error
from getpass import getpass
from datetime import datetime
from threading import Thread
from time import sleep


if not os.path.exists('targets.json'):
	print('Targets file not found, downloading...')
	targets_url = 'https://raw.githubusercontent.com/leolion3/python-red-alert/master/src/targets.json'
	print(subprocess.check_output(f'curl -O {targets_url}', shell=True).decode())

# Debug on by default, turn off if you want to use the app.
DEBUG = True

TELEGRAM_API_KEY = getpass('Input Telegram API Key (Redacted): ')
TELEGRAM_CHAT_ID = getpass('Input Telegram Chat ID (Redacted): ')
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text="

if not DEBUG:
	ROOT_URL = 'https://www.oref.org.il/'
	API_URL = 'https://www.oref.org.il/WarningMessages/alert/alerts.json'
	requests.get(TELEGRAM_URL + 'Api is up and listening...')
else:
	from flask import Flask
	ROOT_URL = 'http://localhost:8080/'
	API_URL = 'http://localhost:8080/alerts.json'

	app = Flask('Testapp')

	@app.route('/', methods=['GET'])
	def test_root():
		return 'OK', 200

	@app.route('/alerts.json', methods=['GET'])
	def test_api():
		with open('example_response.json', 'r', encoding='utf-8') as f:
			data = f.read()
		return bytes(data, 'utf-8')

	def flask_thread():
		app.run(host='localhost', port=8080)


headers = {
   "Host":"www.oref.org.il",
   "Connection":"keep-alive",
   "Content-Type":"application/json",
   "charset":"utf-8",
   "X-Requested-With":"XMLHttpRequest",
   "sec-ch-ua-mobile":"?0",
   "User-Agent":"",
   "sec-ch-ua-platform":"macOS",
   "Accept":"*/*",
   "sec-ch-ua": '".Not/A)Brand"v="99", "Google Chrome";v="103", "Chromium";v="103"',
   "Sec-Fetch-Site":"same-origin",
   "Sec-Fetch-Mode":"cors",
   "Sec-Fetch-Dest":"empty",
   "Referer":"https://www.oref.org.il/12481-he/Pakar.aspx",
   "Accept-Encoding":"gzip, deflate, br",
   "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}

labels = []
region_keys = []
regions = []
monitored_regions = {}
last_response_id = ''
monitor_active = True
emojis = {
	'טיל' : '🚀',
	'כלי טיס' : '✈️'
}


def cache_alert(alert):
	with open('alerts_cache.json', 'a+') as f:
		f.write(json.dumps(alert) + '\n\n')
		f.flush()


def get_actual_cities(cities):
	"""
	Cities are sometimes returned separated by comma.
	This doesnt help our cause when dealing with regions...
	Separate by comma.
	"""
	actual_cities = []
	for city in cities:
		actual_cities.append(city.strip())
	return actual_cities


def is_monitored(cities):
	global monitored_regions, DEBUG
	if DEBUG:
		logging.debug(json.dumps(cities))
		logging.debug(json.dumps(monitored_regions))
	for city in get_actual_cities(cities):
		for key, region in monitored_regions.items():
			if city in region or region in city:
				return True
	return False


def build_telegram_response(event, to_do, cities):
	time = datetime.now().strftime("%H:%M")
	emoji = '⚠️'
	for em in emojis.keys():
		if em in event:
			emoji = emojis[em]
			break
	return f"""
	{'=' * 10} {emoji} ALERT {'=' * 10}\n\n
	{time} {event}\n
	{', '.join(cities)}\n
	{to_do}
	"""


def send_telegram_message(message):
	global TELEGRAM_URL
	url = TELEGRAM_URL + message
	r = requests.get(url)
	if r.status_code == 200:
		logging.info('GET [::] Success!')
	else:
		logging.info('[ERROR] Error sending telegram message!')
		logging.info(f'GET [::] {r.status_code} {r.text}')


def extract_data_and_notify(alert):
	global last_response_id, DEBUG
	if not len(alert):
		if DEBUG:
			logging.error('[DATA EXTRACTION]: Empty data! Data: ' + json.dumps(alert))
		return
	if DEBUG:
		cache_alert(alert)
	report_id = alert['id']
	if report_id == last_response_id and not DEBUG:
		return
	last_response_id = report_id
	event = alert['title']
	to_do = alert['desc']
	cities = alert['data']
	if not is_monitored(cities):
		logging.error('[MONITOR] Not monitored: ' + ', '.join(cities))
		logging.error('[MONITOR] Monitored regions: ' + ', '.join(monitored_regions))
		return
	response = build_telegram_response(event, to_do, cities)
	logging.info('[TELEGRAM]: ' + response)
	if not DEBUG:
		send_telegram_message(response)


def fetch_alert(url, api_url):
	"""
	API apparantly always returns 1 alert...
	"""
	global headers, DEBUG, monitor_active
	s = requests.session()
	r = s.get(url, headers=headers)
	if DEBUG:
		logging.info(f'GET [::] {url} {r.status_code}')
	if not r.status_code == 200:
		monitor_active = False
		error('API unreachable! Are you in Israel?')
		exit(-1)
	r = s.get(api_url, headers=headers)
	if DEBUG:
		logging.info(f'GET [::] /WarningMessages/alert/alerts.json {r.status_code}')
	if not r.status_code == 200:
		return []
	# Alerts are returned as binary data
	# And data apparantly always has a min length of 1...?
	if len(r.content.decode("UTF-8").replace("\n","").replace("\r","")) > 1:
		if DEBUG:
			logging.info(f'"{r.content.decode("UTF-8")}"')
		return json.loads(r.content)
	return []


def search_regions(name):
	global labels
	results = []
	for label in labels:
		if name in label:
			results.append(label)
	return results


def extract_region_keys():
	global regions, region_keys
	for i in range(1, 10000):
		if str(i) in regions:
			region_keys.append(str(i))


def get_labels():
	global regions, region_keys, labels
	for key in region_keys:
		label = regions.get(key).get('label')
		labels.append(f'{key}. {label}')


def load_regions():
	global regions
	with open('targets.json', 'r', encoding='utf-8') as f:
		data = f.read()
	regions = json.loads(data)


def setup():
	load_regions()
	extract_region_keys()
	get_labels()


def help():
	print()
	print('=============== Red Alert Monitor ===============')
	print()
	print('?, help              - Display this menu')
	print('s, search {name}     - Search for a city')
	print('a, add {id}          - Add city to monitor by id')
	print('r, remove {id}       - Remove id from monitor')
	print('l, list              - List active monitors')
	print('exit                 - Terminate monitor')


def list_monitors():
	global monitored_regions
	if not len(monitored_regions):
		print('- No active monitors!')
		print()
		return
	print('> Active monitors:')
	print()
	for key, label in monitored_regions.items():
		print(key, '. ', label)


def remove(key):
	global monitored_regions
	if key in monitored_regions.keys():
		del monitored_regions[key]
		print('> Deleted region', key)
	else:
		print('- No monitor active for region', key)


def search(key):
	result = search_regions(key)
	if not len(result):
		print('No results found for', key)
		return
	print('> Results:')
	for entry in result:
		print(entry)


def add(key):
	global region_keys, regions, monitored_regions
	if not key in region_keys:
		print('- Illegal region key entered! Region keys can only be numbers!')
		return
	else:
		monitored_regions[key] = regions[key].get('label')
		print('> Added', key, 'to monitor!')


def loop():
	global monitor_active, t2
	print()
	try:
		cmd = input('Select action #> ')
		if not monitor_active:
			print('Monitor inactive, terminating...')
			exit(-1)
		print()
		if cmd in ['?', 'help']:
			help()
		elif cmd in ['l', 'list']:
			list_monitors()
		elif cmd == 'exit':
			print('Processing exit, this may take a couple seconds...')
			monitor_active = False
			t2.join()
			print('Monitor thread terminated, exiting...')
			exit(0)
		elif cmd.split(' ')[0] == 'r' or 'remove' in cmd:
			cmd, key = cmd.split(' ')
			remove(key)
		elif cmd.split(' ')[0] == 's' or 'search' in cmd:
			cmd, key = cmd.split(' ')
			search(key)
		elif cmd.split(' ')[0] == 'a' or 'add' in cmd:
			cmd, key = cmd.split(' ')
			add(key)
		else:
			raise Exception()
	except Exception as e:
		print('[ERROR]: Error occurred or wrong command!')
		if DEBUG:
			print(e)
		else:
			print('[*] Trace is disabled.')
	loop()


def ui_thread():
	setup()
	help()
	loop()


def monitor_thread():
	global monitor_active, ROOT_URL, API_URL
	while monitor_active:
		extract_data_and_notify(fetch_alert(ROOT_URL, API_URL))
		sleep(5)


if __name__ == '__main__':
	t1 = Thread(target=ui_thread)
	t2 = Thread(target=monitor_thread)
	t2.setDaemon(True)
	t1.start()
	if DEBUG:
		t3 = Thread(target=flask_thread)
		t3.setDaemon(True)
		t3.start()
	t2.start()
	t1.join()
	t2.join()
	t3.join()