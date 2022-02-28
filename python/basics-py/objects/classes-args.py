class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):       # With the parameter name, arguments can be passed to the object creation
        self.name = name
        print(self.name,'I am constructed, thanks')



    def party(self):
        self.x = self.x + 1
        print(self.name, 'So far', self.x)


x = PartyAnimal('Ian')        
y = PartyAnimal('Paloma')


x.party()
y.party()


