from requests_html import HTMLSession
from bs4 import BeautifulSoup


ADDRESS = "YOUR_ETH_ADDRESS"


def fetch_balance(address):
	
	url = f'https://ethermine.org/miners/{address}/dashboard'
	
	session = HTMLSession()
	
	r = session.get(url)
	r.html.render()

	soup = BeautifulSoup(r.html.raw_html, "html.parser")
	element = soup.find_all("span", class_="current-balance")
	balance = str(element).split('>')[1].split('</')[0]

	return balance


if __name__ == '__main__':
	print(f'Unpaid Balance: {fetch_balance(ADDRESS)}')