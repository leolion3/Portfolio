from requests_html import HTMLSession
import requests
import json
from bs4 import BeautifulSoup

# Used to normalise Ethereum balance 
ETH_NORMAL = 1000000000000000000

# Hashrate Unit (Default is MH)
HASHRATE_UNIT = 1000000

# Digits to display after point in ethereum balances
ETH_DIGITS = 5

# Hashrate Digits to display after point
HASHRATE_DIGITS = 2

# Your ETH Address
ADDRESS = "YOUR_ETH_ADDRESS"

# Your Etherscan API Token
API_TOKEN = 'YOUR_ETHERSCAN_API_TOKEN'

# Your Polyscan API Token
POLY_API_TOKEN = 'YOUR_POLYSCAN_API_TOKEN'

# Wrapped ethereum contract id
WRAPPED_ETHER = '0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619'

# Cache of javascript websites
ethermine_cache = { }

# Ethermine API Cache
ethermine_api_cache = { }


"""
# Loads Javascript content in webpages and then caches them
def get_cached_website(url):
	if url in ethermine_cache:
		return ethermine_cache[url]
	else:
		session = HTMLSession()
		r = session.get(url)
		r.html.render(timeout = 4, sleep = 4)

		ethermine_cache[url] = r.html.raw_html

		return ethermine_cache[url]
"""


# Fetches ethermine api data
def get_cached_ethermine_api_data(url):
	if url in ethermine_api_cache:
		return ethermine_api_cache[url]
	else:
		r = requests.get(url)
		data = json.loads(r.text)
		ethermine_api_cache[url] = data
		return data


def fetch_unpaid(address):
	
	url = f'https://api.ethermine.org/miner/{address}/dashboard'
	
	data = get_cached_ethermine_api_data(url)

	converted = float(data.get('data').get('currentStatistics').get('unpaid')) / ETH_NORMAL

	return round(converted, ETH_DIGITS)


"""
def fetch_payout_date(address):

	url = f'https://ethermine.org/miners/{address}/payouts'
	
	soup = BeautifulSoup(get_cached_website(url), "html.parser")
	elements = soup.find_all("div")
	print(soup)
	for element in elements:
		print(element)
		if 'days' in str(element):
			break

	try:
		print(element)
		next_payout = str(element).split('≈')[1].split('>')[1].split('<')[0]
	except:
		next_payout = "N/A"
		
	return next_payout
"""


def fetch_current_hashrate(address):

	url = f'https://api.ethermine.org/miner/{address}/dashboard'
	
	data = get_cached_ethermine_api_data(url)

	converted = data.get('data').get('currentStatistics').get('currentHashrate') / HASHRATE_UNIT

	return round(converted,HASHRATE_DIGITS)


def fetch_reported_hashrate(address):

	url = f'https://api.ethermine.org/miner/{address}/dashboard'
	
	data = get_cached_ethermine_api_data(url)

	converted = data.get('data').get('currentStatistics').get('reportedHashrate') / HASHRATE_UNIT

	return round(converted,HASHRATE_DIGITS)


def fetch_active_workers(address):

	url = f'https://api.ethermine.org/miner/{address}/dashboard'
	
	data = get_cached_ethermine_api_data(url)

	return data.get('data').get('currentStatistics').get('activeWorkers')


def fetch_valid_shares(address):

	url = f'https://api.ethermine.org/miner/{address}/dashboard'
	
	data = get_cached_ethermine_api_data(url)

	return data.get('data').get('currentStatistics').get('validShares')


def fetch_stale_shares(address):

	url = f'https://api.ethermine.org/miner/{address}/dashboard'
	
	data = get_cached_ethermine_api_data(url)

	return data.get('data').get('currentStatistics').get('staleShares')


def fetch_invalid_shares(address):

	url = f'https://api.ethermine.org/miner/{address}/dashboard'
	
	data = get_cached_ethermine_api_data(url)

	return data.get('data').get('currentStatistics').get('invalidShares')


def fetch_ether_balance(address, api_key):

	url = f'https://api.etherscan.io/api?module=account&action=balance&address=0x{address}&tag=latest&apikey={api_key}'

	r = requests.get(url)

	response_content = json.loads(r.text)

	return round(float(response_content.get('result')) / ETH_NORMAL, ETH_DIGITS)


def fetch_poly_balance(address, api_key, wrapped_eth):
	url = f'https://api.polygonscan.com/api?module=account&action=tokenbalance&contractaddress={wrapped_eth}&address=0x{address}&tag=latest&apikey={api_key}'

	r = requests.get(url)

	response_content = json.loads(r.text)

	return round(float(response_content.get('result')) / ETH_NORMAL, ETH_DIGITS)


def get_ether_price(api_key):
	url = f'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={api_key}'

	r = requests.get(url)

	response_content = json.loads(r.text)

	return response_content.get('result').get('ethusd')


def get_account_statistics():
	global ADDRESS, API_TOKEN, POLY_API_TOKEN, WRAPPED_ETHER
	eth_balance = fetch_ether_balance(ADDRESS, API_TOKEN)
	poly_balance = fetch_poly_balance(ADDRESS, POLY_API_TOKEN, WRAPPED_ETHER)
	total_balance = eth_balance + poly_balance
	balance_USD = round(float(get_ether_price(API_TOKEN)) * total_balance, 2)
	print('--- Account Statistics ---')
	print(f'Account Balance: {str(eth_balance)} ⧫')
	print(f'Polygon Balance: {str(poly_balance)} ⧫')
	print(len(str(poly_balance)) * '-' + '--------------------')
	print(f'Total Balance: {str(total_balance)} ⧫')
	print(f'Total Balance USD: {str(balance_USD)} $\n')


def get_miner_statistics():
	global ADDRESS
	print('--- Miner Statistics ---')
	print(f'Current Hashrate: {fetch_current_hashrate(ADDRESS)} MH/s')
	print(f'Reported Hashrate: {fetch_reported_hashrate(ADDRESS)} MH/s')
	print(f'Unpaid Balance: {fetch_unpaid(ADDRESS)} ⧫')
	print(f'Active Workers: {str(fetch_active_workers(ADDRESS))}')
	print(f'Valid Shares: {str(fetch_valid_shares(ADDRESS))}')
	print(f'Invalid Shares: {str(fetch_invalid_shares(ADDRESS))}')
	print(f'Stale Shares: {str(fetch_stale_shares(ADDRESS))}\n')
	#print(f'Next Payout in: {fetch_payout_date(ADDRESS)} days\n')


if __name__ == '__main__':
	print('===== Ethermine status =====\n')
	get_account_statistics()
	get_miner_statistics()
	print('============================')
