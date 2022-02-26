# Loop through lists verifying if its in the dict and appending if its not

myDict = dict()
myList = ['Ian', 'Paloma', 'Biscoito', 'Thor', 'Kali', 'Minie', 'Ian', 'Thor']

for name in myList:         # Loops all name in the lists
    if name not in myDict:      # If the name in the list is not in the dictionary
        myDict[name] = 1        # Append to the dictionary with the value 1
    else:                        # If it is already in the dicitonary, sum 1 to the key
        myDict[name] = myDict[name] + 1

print(myDict)        # {'Ian': 2, 'Paloma': 1, 'Biscoito': 1, 'Thor': 2, 'Kali': 1, 'Minie': 1}




# Simplifying with get()

myDict2 = dict()
myList2 = ['Ian', 'Paloma', 'Biscoito', 'Thor', 'Kali', 'Minie', 'Ian', 'Thor']

for names in myList2:

    myDict2[names] = myDict2.get(names, 0) + 1                #The get() method provides a default value of zero when the key is not already in the dictionary

print(myDict2)