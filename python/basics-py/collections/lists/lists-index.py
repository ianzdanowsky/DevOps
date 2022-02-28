myList = ['Ian', 'Paloma', 'Biscoito']
print('I love you {0}'.format(myList[1])) # I love you Paloma

# Lists are mutable

myList[0] = 'Russo'
print(myList) # ['Russo', 'Paloma', 'Biscoito']

# Lenght of the list

listLeng = len(myList)
print(listLeng) # 4