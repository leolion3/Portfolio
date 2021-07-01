#!/bin/usr/env python3
from requests_html import HTMLSession
import requests
import json
from bs4 import BeautifulSoup


# Your ETH Address
ADDRESS = "YOUR_ETH_ADDRESS"
# Your Etherscan API Token
API_TOKEN = 'YOUR_ETHERSCAN_API_KEY'
# Cache of javascript websites
ethermine_cache = { }


def get_cached_website(url):
	if url in ethermine_cache:
		return ethermine_cache[url]
	else:
		session = HTMLSession()
	
		r = session.get(url)
		r.html.render(timeout = 0, sleep = 5)

		ethermine_cache[url] = r.html.raw_html

		return ethermine_cache[url]


def fetch_unpaid(address):
	
	url = f'https://ethermine.org/miners/{address}/dashboard'
	
	soup = BeautifulSoup(get_cached_website(url), "html.parser")
	element = soup.find_all("span", class_="current-balance")
	balance = str(element).split('>')[1].split('</')[0]

	return balance


def fetch_payout_date(address):

	url = f'https://ethermine.org/miners/{address}/payouts'
	
	soup = BeautifulSoup(get_cached_website(url), "html.parser")
	elements = soup.find_all("div", class_="workers card")

	for element in elements:
		if 'Next Payout' in str(element):
			break

	next_payout = str(element).split('≈')[1].split('>')[1].split('<')[0]

	return next_payout


def fetch_current_hashrate(address):

	url = f'https://ethermine.org/miners/{address}/dashboard'

	soup = BeautifulSoup(get_cached_website(url), "html.parser")
	elements = soup.find_all("div", class_="tooltip")

	for element in elements:
		if '(MH/s)' in str(element):
			break

	element = ''.join(str(element).split('>MH/s')[0].split('</')[:-1]).split('>')[-1]

	return element


def fetch_reported_hashrate(address):

	url = f'https://ethermine.org/miners/{address}/dashboard'

	soup = BeautifulSoup(get_cached_website(url), "html.parser")
	elements = soup.find_all("div", class_="tooltip")

	for element in elements:
		if 'Reported' in str(element):
			break

	element = str(element).split('<span')[2].split('>')[1].split('<')[0] 

	return element


def fetch_ether_balance(address, api_key):

	url = f'https://api.etherscan.io/api?module=account&action=balance&address=0x{address}&tag=latest&apikey={api_key}'

	r = requests.get(url)

	response_content = json.loads(r.text)

	# result needs to be divided by 10^18 to gain actual eth balance
	return float(response_content.get('result')) / 1000000000000000000


if __name__ == '__main__':
	print('===== Ethermine status =====\n')
	print(f'Current Hashrate: {fetch_current_hashrate(ADDRESS)} MH/s')
	print(f'Reported Hashrate: {fetch_reported_hashrate(ADDRESS)} MH/s')
	print(f'Unpaid Balance: {fetch_unpaid(ADDRESS)} ⧫')
	print(f'Next Payout in: {fetch_payout_date(ADDRESS)} days')
	print(f'Account Balance: {str(fetch_ether_balance(ADDRESS, API_TOKEN))[0:6]} ⧫\n')
	print('============================')