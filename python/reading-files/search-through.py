fhand = open('/home/ianzpimentel/myLearning/python/reading-files/mbox.txt')

for line in fhand:
    line = line.rstrip() # Remove whitespaces at the right (\n in this case) - Very common
    if line.startswith("From:"): # Look for the lines that starts with "From:"
        print(line)



# Skipping criteria - if not

fhand2 = open('/home/ianzpimentel/myLearning/python/reading-files/mbox.txt')

for line in fhand2:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)