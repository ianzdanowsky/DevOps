fileH = open('/home/ianzpimentel/myLearning/python/reading-files/mbox.txt')

readFile = fileH.read() # Read the file as a block separated with \n

print(len(readFile))

print(readFile[:20])