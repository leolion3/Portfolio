from requests_html import HTMLSession
from bs4 import BeautifulSoup


ADDRESS = "YOUR_ETH_ADDRESS"


def fetch_balance(address):
	
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


if __name__ == '__main__':
	print('====== Ethermine status =====\n')
	print(f'Unpaid Balance: {fetch_balance(ADDRESS)} ⧫')
	print(f'Next Payout in: {fetch_payout_date(ADDRESS)} days\n')
	print('=============================')