import urllib.request, urllib.parse, urllib.error
import requests

from bs4 import BeautifulSoup


r = requests.get("https://getedu.com.br/")
soup = BeautifulSoup(r.content, features="lxml")


print(soup)

for a_tag in soup.find_all('a', class_='listing-name', href=True):
        print('href: ', a_tag['href'])