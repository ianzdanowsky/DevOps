data = 'From ian@gsaladeaula.com.br Fri Feb  25  15:40:00  2022'

dataStart = data.find('@')
print(dataStart)

dataStart2 = data.find(' ',dataStart)
print(dataStart2)

domain = data[dataStart+1:dataStart2]
print(domain)