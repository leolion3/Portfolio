#!/usr/bin/env python3
import requests
import json
import getpass
from urllib.parse import quote


username = getpass.getpass('Enter username (hidden): ')
password = getpass.getpass('Enter password (hidden): ')


def initial_comm(s: requests.Session):
	url = 'https://finanzblickx.buhl.de/login'
	r = s.get(url)
	print(r.status_code, '[::]', url)


def login(s: requests.Session):
	global username, password
	print('Performing login...')
	url = 'https://www.buhl.de/mein-buhlkonto/wp-json/api/v1/login'
	data = {
		'action': 'LoginUser',
		'post_type': 'POST',
		'eml-user': username,
		'psw-user': password,
		'passed-get-param': 'uc=trIec2ruhEpHL&nt=true&dm_finanzblick=0&app=Finanzblick',
		'passed-ls-param': '',
		'rdr-buhlparam': 1040101
	}
	r = s.post(url, data=data)
	print(r.status_code, '[::]', url)

	url_pattern = '<form action=\"'
	url_end_pattern = '\" method=\"post\"'
	js = r.json()
	redirect = js['redirection'].split(url_pattern)[1].split(url_end_pattern)[0]
	ticket_pattern = 'value=\"'
	ticket_end_pattern = '\" name=\"BuhlTicket\"'
	ticket = js['redirection'].split(ticket_pattern)[1].split(ticket_end_pattern)[0]
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Host': 'finanzblickx.buhl.de',
		'Origin': 'https://www.buhl.de',
		'Referer': 'https://www.buhl.de/'
	}
	data = {
		'BuhlTicket': ticket
	}
	r = requests.post(redirect, headers=headers, data=data, allow_redirects=False)
	print(r.status_code, '[::]', redirect)

	if r.status_code == 302:
		location_header = r.headers.get('Location')
		r = s.get(location_header)
		print(r.status_code, '[::]', location_header)
		login_url = f'https://finanzblickx.buhl.de/login?ticket={quote(ticket)}&dm_finanzblick=0&app=Finanzblick'
		r = s.get(login_url)
		print(r.status_code, '[::]', login_url)
		# Actual auth
		url = 'https://finanzblickx.buhl.de/api/auth/user/loginWithTicket'
		data = {
			"accessToken": ticket
		}
		r = s.post(url, json=data)
		print(r.status_code, '[::]', url)
		print('Token retrieved.')
		return r.json()['token']
	
	print('No redirect found, terminating...')
	exit()


def get_bank_details(cookie):
	"""
	TODO adjust as needed.
	"""
	url = "https://finanzblickx.buhl.de/api/accounts/accountbases"
	headers = {
		'Authorization': f'Bearer {cookie}'
	}
	r = requests.get(url, headers=headers)
	data = r.json()
	return data[0]['balance']


def get_cookie():
	s = requests.Session()
	s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
	initial_comm(s)
	return login(s)


demo_balance = get_bank_details(get_cookie())
print(demo_balance)