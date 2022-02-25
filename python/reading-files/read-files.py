fileHandler = open('/home/ianzpimentel/myLearning/python/reading-files/mbox.txt') # Get to the file, "opens the book"

print(fileHandler) # Show encoding, mode (r,w)

for line in fileHandler: # Loop through all the lines and print below
    print(line)
