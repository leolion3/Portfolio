# Note: fetching the payout date is momentarily not possible
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
API_TOKEN = 'YOUR_ETHERSCAN_API_KEY'

# Cache of javascript websites
ethermine_cache = { }

# Ethermine API Cache
ethermine_api_cache = { }


# Loads Javascript content in webpages and then caches them
def get_cached_website(url):
	if url in ethermine_cache:
		return ethermine_cache[url]
	else:
		session = HTMLSession()
	
		r = session.get(url)
		r.html.render(timeout = 0, sleep = 1)

		ethermine_cache[url] = r.html.raw_html

		return ethermine_cache[url]


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


# Momentarily not working
def fetch_payout_date(address):

	url = f'https://ethermine.org/miners/{address}/payouts'
	
	soup = BeautifulSoup(get_cached_website(url), "html.parser")
	elements = soup.find_all("div", class_="workers card")

	for element in elements:
		if 'Next Payout' in str(element):
			break

	try:
		next_payout = str(element).split('≈')[1].split('>')[1].split('<')[0]
	except:
		next_payout = "N/A"
		
	return next_payout


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

	# result needs to be divided by 10^18 to gain actual eth balance
	return round(float(response_content.get('result')) / ETH_NORMAL, ETH_DIGITS)


if __name__ == '__main__':
	print('===== Ethermine status =====\n')
	print(f'Account Balance: {str(fetch_ether_balance(ADDRESS, API_TOKEN))} ⧫\n')
	print(f'Current Hashrate: {fetch_current_hashrate(ADDRESS)} MH/s')
	print(f'Reported Hashrate: {fetch_reported_hashrate(ADDRESS)} MH/s')
	print(f'Unpaid Balance: {fetch_unpaid(ADDRESS)} ⧫')
	print(f'Active Workers: {str(fetch_active_workers(ADDRESS))}')
	print(f'Valid Shares: {str(fetch_valid_shares(ADDRESS))}')
	print(f'Invalid Shares: {str(fetch_invalid_shares(ADDRESS))}')
	print(f'Stale Shares: {str(fetch_stale_shares(ADDRESS))}\n')
	#print(f'Next Payout in: {fetch_payout_date(ADDRESS)} days\n')
	print('============================')
