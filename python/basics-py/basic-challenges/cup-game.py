from random import shuffle
from re import M

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def user_input():
    guess = ""

    while guess not in ['0','1','2']:
        guess = input("Please tell me a number from 0 - 2:")

    return int(guess)


def check_match(list,guess):
    if list[guess] == "O":
        print("Correct")
    else:
        print(list)



mylist = [" ","O"," "]

myShuffledList = shuffle_list(mylist)

# print(myShuffledList)

guess = user_input()

#print(guess)

check_match(myShuffledList,guess)

