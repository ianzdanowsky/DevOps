myDict = dict() # Can use { } for the construction

myDict['money'] = 12
myDict['biscoito'] = 2
myDict['salário'] = 3000

print(myDict) # {'money': 12, 'biscoito': 2, 'salário': 3000}

print(myDict['biscoito']) # 2

myDict['salário'] = myDict['salário'] + 3000
print(myDict['salário']) # 6000