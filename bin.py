import requests
from bs4 import BeautifulSoup

statsres = requests.get('https://pool.binance.com/en/statistics?urlParams=8U5iZ6hqH6hFmriaB0I0Rh5bZuWHncJdewOFYrvlUBI03876')
earningres = requests.get('https://pool.binance.com/en/earnings?urlParams=8U5iZ6hqH6hFmriaB0I0Rh5bZuWHncJdewOFYrvlUBI03876')

statsres = requests.get('https://pool.binance.com/mining-api/v1/public/pool/stat?observerToken=8U5iZ6hqH6hFmriaB0I0Rh5bZuWHncJdewOFYrvlUBI03876')

        
# print(earnsoup.prettify())