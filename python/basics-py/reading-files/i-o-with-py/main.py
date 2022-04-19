

with open('myfile.txt', mode='w') as myfile:
    openfile = myfile.read() # Everything as a string
    # openfile = myfile.readlines() # Every line is a item of a list



print(openfile)