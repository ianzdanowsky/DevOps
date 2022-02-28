import re

x = 'I want to eat a hamburguer because i have to eated'
y = re.findall('eat', x)

print(y)