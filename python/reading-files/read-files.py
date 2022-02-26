
# Get to the file, "opens the book"
fileHandler = open('/home/ianzpimentel/myLearning/python/reading-files/mbox.txt') 


# Show encoding, mode (r,w)
print(fileHandler) 


# Loop through all the lines and print below
for line in fileHandler: 
    print(line)


# Returns to the begin of the file (byte 0)
fileHandler.seek(0)


# Count lines in a file
count = 0
for line in fileHandler:
    count = count + 1
print('Line count:', count)
