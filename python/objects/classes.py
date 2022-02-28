# class -> a template
# attribute -> a variable within a class
# method -> a function within a class
# object -> a particular instance of a class
# constructor -> code that runs when the object is created
# inheritance -> the ability to extend a class to make a new one


# Contructs the class parameteres

class PartyAnimal:
    x = 0


    def __init__(self):         #__init__ is a function called automatically when the object is build
        print('I am constructed, thanks')



    def party(self):
        self.x = self.x + 1
        print('So far', self.x)


    def __del__(self):
        print('I am desconstructed, omg!')

# Creates the object from the class

an = PartyAnimal()         # will start the __init__ method

# Uses the method party() from the class in the object constructed

an.party()
an.party()

# Desconstruct the object by setting other value to the variable 'an'

an = 50         # Will start the __del__ method


