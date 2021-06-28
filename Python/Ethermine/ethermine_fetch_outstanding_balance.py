#!/bin/usr/env python3
from requests_html import HTMLSession
import requests
import json
from bs4 import BeautifulSoup


# Your ETH Address
ADDRESS = "YOUR_ETH_ADDRESS"
# Your Etherscan API Token
API_TOKEN = 'YOUR_ETHERSCAN_API_KEY'


def fetch_unpaid(address):
	
	url = f'https://ethermine.org/miners/{address}/dashboard'
	
	session = HTMLSession()
	
	r = session.get(url)
	r.html.render(timeout = 0, sleep = 1)

	soup = BeautifulSoup(r.html.raw_html, "html.parser")
	element = soup.find_all("span", class_="current-balance")
	balance = str(element).split('>')[1].split('</')[0]

	return balance


def fetch_payout_date(address):

	url = f'https://ethermine.org/miners/{address}/payouts'
	
	session = HTMLSession()
	
	r = session.get(url)
	r.html.render(timeout = 0, sleep = 1)

	soup = BeautifulSoup(r.html.raw_html, "html.parser")
	elements = soup.find_all("div", class_="workers card")

	for element in elements:
		if 'Next Payout' in str(element):
			break

	next_payout = str(element).split('≈')[1].split('>')[1].split('<')[0]

	return next_payout


def fetch_ether_balande(address, api_key):

	url = f'https://api.etherscan.io/api?module=account&action=balance&address=0x{address}&tag=latest&apikey={api_key}'

	r = requests.get(url)

	response_content = json.loads(r.text)

	# result needs to be divided by 10^18 to gain actual eth balance
	return float(response_content.get('result')) / 1000000000000000000


if __name__ == '__main__':
	print('===== Ethermine status =====\n')
	print(f'Unpaid Balance: {fetch_unpaid(ADDRESS)} ⧫')
	print(f'Next Payout in: {fetch_payout_date(ADDRESS)} days')
	print(f'Account Balance: {str(fetch_ether_balande(ADDRESS, API_TOKEN))[0:6]} ⧫\n')
	print('============================')