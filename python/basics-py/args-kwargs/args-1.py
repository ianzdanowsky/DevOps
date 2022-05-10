#Fucntion that returns a list containg only those arguments that are even


def myfunc(*args):
    mylist = []
    
    for arg in args:
        if isinstance(arg,int) == True:
            if arg % 2 == 0:
                mylist.append(arg)
        else:
            print("This function accepts only integers")
        
    print(mylist)



myfunc(10,50,30,55,33,21,'bola')