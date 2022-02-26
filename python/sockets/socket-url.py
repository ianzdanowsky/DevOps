import urllib.request, urllib.parse, urllib.error       # Import urllib for handling http requests

fileHandler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')      # Request a http get to the server

for line in fileHandler:        # Loop thorugh each line in the server response
    print(line.decode().split())    # Decode, split it into a list and print out