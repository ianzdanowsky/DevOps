import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('-')
html = urllib.request.urlopen(url).read()       # Read the html as a block, not looping through lines

soup = BeautifulSoup(html, 'html.parser')       # BeautifulSoup knows about bytes and UTF-8. Adjust results to receive queries.


# Retrieve all anchors tag from the page

tags = soup('a')          # Query in the BeautifulSoup

for tag in tags:
    print(tag.get('href', None))    # Print the href link of the anchor tags in the page