import requests
import json
import logging
import os
import getpass
logging.basicConfig(level=logging.DEBUG)

from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler


DEBUG = False
if not DEBUG:
    TOKEN = getpass.getpass('Enter Telegram API Key:')
    CHAT_ID = getpass.getpass('Enter Telegram Chat ID:')
    TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="
street = getpass.getpass('Input street (capitalized):')
house_number = getpass.getpass('Input house number:')
backend_url = 'https://www.die-bremer-stadtreinigung.de/api/c-trace/app/garbage-calendar-web'

translated_names = {
    "pine" : {
        "Deutsch": "Weihnachtsbaum",
        "English": "Christmas Tree"
    },
    "residual": {
        "Deutsch": "Restmüll",
        "English": "Residual"
    },
    "organic": {
        "Deutsch": "Bio",
        "English": "Organic"
    },
    "yellow-bag": {
        "Deutsch": "Gelber Sack",
        "English": "Yellow bag"
    },
    "paper": {
        "Deutsch": "Papier",
        "English": "Paper"
    }
}


def __fetch_data(house_number: str, street: str) -> {}:
    """
    Fetch data from the api for the given month.
    """
    global backend_url
    month = datetime.now().strftime('%Y-%m')
    logging.info('Fetching data from API...')
    address_payload = {
        'firstMonth': month,
        'houseNo': house_number,
        'street': street
    }
    r = requests.post(backend_url, data=address_payload)
    if not r.text:
        logging.error('Incorrect address or no data found!')
        return {'list': ''}
    return json.loads(r.text).get('list')


def __get_tomorrow():
    """
    Get the next day, formatted as YYYY-mm-dd.
    """
    return (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')


def __validate_data(data: str, tomorrow: str) -> bool:
    """
    Validate the data retrieved from the api.
    """
    return data is not None and tomorrow in data
        

def __convert_trash_to_string(trash: str, lang: str) -> str:
    """
    Get readable names for trash types.
    """
    global translated_names
    converted = translated_names.get(trash)
    if converted is not None:
        if converted is not None:
            return converted.get(lang)
    return trash


def __get_altered(data: str, tomorrow: str, message: str, lang: str) -> str:
    """
    Get any schedule alterations.
    """
    altered = data.get(tomorrow).get('hasAltered')
    if not altered:
        return message
    langs = {
        'Deutsch': '\n(*) Es gab eine Änderung in dem Abfallkalendar:\n- Der {0} abfall Abholtermin wurde verschoben.\n',
        'English': '\n(*) The trash schedule has been altered:\n- The {0} trash schedule was changed.\n'
    }
    for waste_type in waste:
        if waste_type.get('isAltered'):
            message += langs.get(lang).format(__convert_trash_to_string(waste_type.get('type'), lang))
    message += '\n'
    return message


def __get_waste(data: str, tomorrow: str, message: str, lang: str) -> str:
    langs = {
        'Deutsch': """- Der {0} müll wird morgen abgeholt!\n""",
        'English': """- The {0} is being picked up tomorrow!\n"""
    }
    waste = data.get(tomorrow).get('waste')
    for waste_type in waste:
        message += langs.get(lang).format(__convert_trash_to_string(waste_type.get('type'), lang))
    return message


def __get_multilingual_report(data: str, tomorrow: str) -> str:
    """
    Get trash report in multiple languages.
    """
    LANGUAGES = {
        'Deutsch': 'Abfallansage für Morgen:\n',
        'English': 'Waste report for tomorrow:\n'
    }
    message = ''
    for lang, intro in LANGUAGES.items():
        message += ('=' * 10 + ' ' + lang + ' ' + '=' * 10 + '\n\n')
        message += intro
        message = __get_altered(data, tomorrow, message, lang)
        message = __get_waste(data, tomorrow, message, lang)
        message += '\n'
    return message


def __scheduler(house_number: str, street: str) -> str:
    """
    Scheduler that exeutes once a day to check the schedule.
    """
    tomorrow = __get_tomorrow()
    data = __fetch_data(house_number, street)
    if not __validate_data(data, tomorrow):
        return ''
    return __get_multilingual_report(data, tomorrow)


def __send_message(house_number: str, street: str) -> None:
    global TELEGRAM_URL, TOKEN, CHAT_ID
    message = __scheduler(house_number, street)
    if not len(message):
        print('No data available for tomorrow!')
        return
    if DEBUG:
        print(message)
        return
    r = requests.get(f'{TELEGRAM_URL}{message}')


def scheduled():
    __send_message(house_number, street)


if __name__ == '__main__':
    if DEBUG:
        scheduled()
        exit(0)
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled, 'cron', hour=18, minute=0)
    msg = f'Scheduler initialised and listening for address: {street} {house_number}'
    r = requests.get(f'{TELEGRAM_URL}{msg}')
    try:
        print('Executing test run...')
        __send_message(house_number, street)
        print('Test run complete, starting scheduler...')        
        scheduler.start()
    except KeyboardInterrupt:
        pass
