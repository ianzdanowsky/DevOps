myDict = {'a':10, 'c':1, 'b':3}
myList = []

for k,v in (myDict.items()):        # Loops in the key value pairs extracted from the dict by the .items() method
    myList.append((v,k))                # Append sorted key value pairs IN REVERSE (v, k) extracted from the dict to the list

print(myList)

myList = sorted(myList, reverse=True)       # Sort the tuple list in a reverse order

print(myList)