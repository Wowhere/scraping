import requests
import sys
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept':'text/html,application/xhtml+xml,application/xml',
           'Pragma': 'no-cache',
           'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin'}

response_text = requests.get(sys.argv[1], headers=headers).text  #python bgpscrep.py https://bgp.he.net/AS22612
#print(response_text)
soup = BeautifulSoup(response_text, 'html.parser')
links = soup.findAll('a')
subnet_links = []
for link in links:
    if str(link).find('/net/') != -1:
        subnet_links.append(link.get_text())
for subnet in subnet_links:
    print(subnet)