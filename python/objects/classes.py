
# Contructs the class parameteres

class PartyAnimal:
    x = 0


    def __init__(self):
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


