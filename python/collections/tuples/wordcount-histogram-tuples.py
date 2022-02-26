fileName = input('Hey user, please tell me the file path:')
fileHandler = open(fileName)

myDict = dict()     # Construct and empty dictionary

for line in fileHandler:           # Loops thorugh each line of the file
    textLines = line.split()        # Split each line into words
    for word in textLines:          # Loop the words in the lines
        myDict[word] = myDict.get(word, 0) + 1         # Verify if its already on myDict or no (0), append

tupleLists = list()             #Create and empty list
for key,value in myDict.items():           #Loop through 2 variables in key value pairs of the dict (.items())
    modTuple = (value, key)         # Modify the order of the tuple, values first
    tupleLists.append(modTuple)      # Append to the empty list the modified tuple 

tupleLists = sorted(tupleLists, reverse=True)        # Sorts the lists of tuples in a reverse order

for val, key in tupleLists[:10]:        # Loops through the first (biggest) key value pairs in the list of tuples
    print(val, key)      