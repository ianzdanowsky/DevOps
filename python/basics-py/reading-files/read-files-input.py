docName = input('Olá, digite o nome do arquivo:\n ')

try:
    fhand = open(docName)
except:
    print('File cannot been opened {0}'.format(docName)) # Avoid error message in the program
    quit()


count = 0

for lines in fhand:
    if lines.startswith('Subject:'): # Count lines starting with 'Subject:'
        count += 1
print('There were {0} lines starting with Subject: in {1}'.format(count,docName))