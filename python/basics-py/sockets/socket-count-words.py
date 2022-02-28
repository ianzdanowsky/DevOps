import urllib.request, urllib.parse, urllib.error       # Import urllib for handling http requests

fileHandler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')      # Request a http get to the server

myDict = dict()

for line in fileHandler:        # Loop thorugh each line in the server response
   words = line.decode().split()   # Decode, split it into a list of words and stores in words
   for word in words:           # Loop through all the words
        myDict[word] = myDict.get(word, 0) + 1      # Verify if the words is in the dict, add if its not

print(myDict)