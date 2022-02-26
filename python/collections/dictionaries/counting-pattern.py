myDict = dict()

print('Hey user, please enter a text:')
userText = input('')

wordsText = userText.split()        # Takes the user input and transforms into a list

print('These are the words:', wordsText)    # Show the user the words in a list format

print('We are counting right now, please wait')

for word in wordsText:             # Loop through all the words in the list wordsText
    myDict[word] = myDict.get(word, 0) + 1         # Checks if a word already exists in the dictionary. If does, 'word' + 1, if its not, 0 + 1.

print('Counts', myDict)