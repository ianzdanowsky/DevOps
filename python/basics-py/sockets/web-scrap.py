import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = str(input('-'))

html = urllib.request.urlopen(url).read()       # Read the html as a block, not looping through lines

soup = BeautifulSoup(html, 'html.parser')       # BeautifulSoup knows about bytes and UTF-8. Adjust results to receive queries.

for link in soup.find_all('a'):
    lines = str(link.get('href'))
    if lines.startswith('http'):
        print(lines)
