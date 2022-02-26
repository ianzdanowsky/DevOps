docName = input('Olá, digite o nome do arquivo:\n ')

fhand = open(docName)
count = 0

for lines in fhand:
    if lines.startswith('Subject:'):
        count += 1
print('There were {0} lines starting with Subject: in {1}'.format(count,docName))