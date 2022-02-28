fileName = input('Please, enter the file path:')            # Gets the file path
fileHandler = open(fileName)            # Open the file

myDict = dict()             # Construct the dictionary

for lines in fileHandler:       # Loop all the lines in the file
    fileLines = lines.split()       # Split the lines into lists
    for words in fileLines:         # Loop all the words in the list
        myDict[words] = myDict.get(words, 0) + 1        # Verify if it exists in the dicitonary, append with 1 if dont, count 1 if does.

bigcount = None
bigword = None

for word,count in myDict.items():       # Two iterables in the myDict dictonary (must use .items())
    if bigcount is None or count > bigcount:           # Checks for the biggest word count and stores it in 'bigcount'
        bigword = word
        bigcount = count

print(bigword, bigcount)