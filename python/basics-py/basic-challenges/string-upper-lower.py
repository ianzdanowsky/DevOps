
#Receives a param and return a string with UpPer and LoWeR CaSe


def myfunc(param):

    formatted_list = ""


    word_letters = list(param)

    for word in word_letters:
        if word_letters.index(word) % 2 == 0:
            upper_word = word.upper()
            formatted_list += upper_word
        else:
            lower_word = word.lower()
            formatted_list += lower_word


    print(formatted_list)




myfunc("MochiLaQUEBRADA")