#!/usr/bin/env python3
# pip install html2image
from html2image import Html2Image
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from datetime import datetime, date, timedelta
import calendar
from typing import List
import getpass
import os


API_URL = 'https://www.die-bremer-stadtreinigung.de/api/c-trace/app/garbage-calendar-web'

street = getpass.getpass('Enter street name (hidden): ')
house_number = getpass.getpass('Enter house number (hidden): ')
TOKEN = getpass.getpass('Enter Telegram API Key:')
CHAT_ID = getpass.getpass('Enter Telegram Chat ID:')
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
TELEGRAM_TEXT_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="


payload = {
	'firstMonth': datetime.now().strftime('%Y-%m'),
	'houseNo': house_number,
	'street': street
}

HTML_FILE = 'template.html'
HTML_OUTPUT = 'generated.html'
PNG_OUTPUT = 'generated.png'
CSS_FILE_1 = 'default.css'
CSS_FILE_2 = 'app.css'

NOT_CURRENT_MONTH = """
<div class="bg-gray-10 rounded p-1 aspect-square">
   <div class="relative h-full flex flex-col justify-between">
      <div class="text-gray-60 ml-4 mt-4 sm:ml-4 sm:mt-4 font-bold text-calendar-sm lg:text-calendar-lg">DATE_PLACEHOLDER</div>
      <div class="flex justify-center items-center gap-0.5 lg:gap-2">
      	ICON_PLACEHOLDER
      </div>
   </div>
</div>
"""

CURRENT_MONTH_TEMPLATE = """
<div class="bg-white rounded p-1 aspect-square">
   <div class="relative h-full flex flex-col justify-between">
      <div class="text-black ml-4 mt-4 sm:ml-4 sm:mt-4 font-bold text-calendar-sm lg:text-calendar-lg">DATE_PLACEHOLDER</div>
      <div class="flex justify-center items-center gap-0.5 lg:gap-2">
      	ICON_PLACEHOLDER
      </div>
   </div>
</div>
"""

ICON_TEMPLATE = """
<span class="flex flex-nowrap justify-center items-center rounded-full w-8 h-8 lg:w-16 lg:h-16"><img class="w-fit" src="ICON_REF" alt=""></span>
"""

ALTERED_ICON = """
<div class="flex justify-center items-center w-5 lg:w-10 h-5 lg:h-10 font-bold text-negative border-2 border-negative rounded-full">!</div>
"""

ICON_MAP = {
	'residual': 'media/DBS_Restmuell.png',
	'organic': 'media/DBS_Biomuell.png',
	'paper': 'media/DBS_Papier_Pappe.png',
	'yellow-bag': 'media/DBS_Verkaufsverpackungen.png',
	'pine': 'media/DBS_Tannenbaum.png'
}


def convert_dates_to_digits(dates: List[datetime]) -> List[int]:
	return [int(d.strftime('%d')) for d in dates]


def get_last_month_dates(first_day: int) -> List[int]:
	today = date.today()
	first = today.replace(day=1)
	last_day = int((first - timedelta(days=1)).strftime('%d')) + 1
	date_range = [i for i in range(last_day - first_day, last_day)]
	return [first-timedelta(days=d) for d in range(1, len(date_range) + 1)][::-1]


def get_next_month_dates(last_day: date) -> List[datetime]:
	days = 6 - last_day.weekday()
	if days == 0:
		return []
	return [last_day + timedelta(days=i) for i in range(1, days + 1)]


def get_first_day_of_month() -> int:
	today = date.today()
	return today.replace(day=1).weekday()


def last_day_of_current_month() -> date:
	today = date.today()
	last_day = calendar.monthrange(today.year, today.month)[1]
	return date(today.year, today.month, last_day)

def format_non_current(dates: List[int]) -> List[str]:
	global NOT_CURRENT_MONTH
	return [NOT_CURRENT_MONTH.replace('DATE_PLACEHOLDER', str(i)) for i in dates]


def format_current(dates: List[int]) -> List[str]:
	global CURRENT_MONTH_TEMPLATE
	return [CURRENT_MONTH_TEMPLATE.replace('DATE_PLACEHOLDER', str(i)) for i in dates]


def generate_template(last_month_dates: List[int], current_month_dates: List[int], next_month_dates: List[int]) -> List[str]:
	output = []
	output.extend(format_non_current(last_month_dates))
	output.extend(format_current(current_month_dates))
	output.extend(format_non_current(next_month_dates))
	return output


def format_weekends(html_template: List[str]) -> List[str]:
	modified = []
	weekday_counter = 0
	for entry in html_template:
		if weekday_counter > 4:
			modified.append(entry.replace('bg-white', 'bg-neutral-300').replace('bg-gray-10', 'bg-neutral-300'))
		else:
			modified.append(entry)
		weekday_counter += 1
		if weekday_counter == 7:
			weekday_counter = 0
	return modified


def get_current_month_dates(last_day: date, days: List[int]):
	today = date.today()
	return [today.replace(day=i) for i in days]


def get_altered_icon() -> str:
	global ALTERED_ICON
	return ALTERED_ICON


def get_trash_icon(name: str) -> str:
	global ICON_TEMPLATE, ICON_MAP
	return ICON_TEMPLATE.replace('ICON_REF', ICON_MAP.get(name) or '')


def make_api_call(date_list: List[datetime], templates: List[str]) -> List[str]:
	global API_URL, payload
	r = requests.post(API_URL, data=payload).json()
	data = r['list']
	for i in range(len(date_list)):
		c_date = date_list[i].strftime('%Y-%m-%d')
		icons = ''
		if c_date in data:
			altered = data[c_date]['hasAltered']
			if altered:
				icons += get_altered_icon()
			for waste in data[c_date]['waste']:
				name = waste['type']
				icons += get_trash_icon(name)
			templates[i] = templates[i].replace('ICON_PLACEHOLDER', icons)
		else:
			templates[i] = templates[i].replace('ICON_PLACEHOLDER', '')
	return templates


def generate_range() -> List:
	first_day: int = get_first_day_of_month()
	last_day: date = last_day_of_current_month()
	last_month_dates: List[datetime] = get_last_month_dates(first_day)
	next_month_dates: List[datetime] = get_next_month_dates(last_day)
	current_month_date_range: List[int] = list(range(1, int(last_day.strftime('%d')) + 1))
	current_month_dates: List[datetime] = get_current_month_dates(last_day, current_month_date_range)
	templates = generate_template(convert_dates_to_digits(last_month_dates), current_month_date_range, convert_dates_to_digits(next_month_dates))
	templates = format_weekends(templates)
	date_list = last_month_dates + current_month_dates + next_month_dates
	templates = make_api_call(date_list, templates)
	return '\n'.join(templates)


def replace_paths(data: str) -> str:
	ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
	return data.replace('media/', ROOT_DIR + '/media/')


def generate_html():
	global HTML_FILE, HTML_OUTPUT
	cal = generate_range()
	with open(HTML_FILE, 'r') as f:
		data = f.read()
	data = data.replace('CALENDAR_PLACEHOLDER', cal)
	data = data.replace('SELECTED_MONTH_PLACEHOLDER', datetime.today().strftime('%B %Y'))
	with open(CSS_FILE_1, 'r') as f:
		css_data = f.read() + '\n'
	with open(CSS_FILE_2, 'r') as f:
		css_data += f.read() + '\n'
	data = data.replace('CSS_PLACEHOLDER', css_data)
	data = replace_paths(data)
	return data


def send_telegram_message():
	global TELEGRAM_URL, TELEGRAM_TEXT_URL, PNG_OUTPUT, CHAT_ID
	r = requests.get(f'{TELEGRAM_TEXT_URL}This month\'s schedule:')
	with open(PNG_OUTPUT, 'rb') as photo:
		files = {'photo': photo}
		data = {'chat_id': CHAT_ID}
		response = requests.post(TELEGRAM_URL, files=files, data=data)
		if response.status_code == 200:
			print('Schedule sent!')
		else:
			print('Error occurred! Trace:', response.text)


def generate_image():
	global HTML_OUTPUT, PNG_OUTPUT
	html = generate_html()
	if os.path.isfile(PNG_OUTPUT):
		os.remove(PNG_OUTPUT)
	hti = Html2Image(size=(1200, 1080))
	hti.screenshot(html_str=html, save_as=PNG_OUTPUT)
	send_telegram_message()


if __name__ == '__main__':
	scheduler = BlockingScheduler()
	scheduler.add_job(generate_image, 'cron', day=1, hour=12, minute=0)
	msg = f'Calendar scheduler initialised and listening for address: {street} {house_number}'
	r = requests.get(f'{TELEGRAM_TEXT_URL}{msg}')
	try:
	  print('Executing test run...')
	  generate_image()
	  print('Test run complete, starting scheduler...')        
	  scheduler.start()
	except KeyboardInterrupt:
	  pass
