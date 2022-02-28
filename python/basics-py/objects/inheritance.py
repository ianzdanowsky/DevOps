class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, name):   
        self.name = name
        print(self.name,'I am constructed, thanks')



    def party(self):
        self.x = self.x + 1
        print(self.name, 'So far', self.x)


class FootballFan(PartyAnimal):           # FootballFan inherits the PartyAnimal class with all methods and parameters
    teamPoints = 0

    def touchdown(self):
        self.teamPoints = self.teamPoints + 7
        self.party()
        print(self.name,"with",self.teamPoints)



object1 = FootballFan('Ian')
object1.touchdown()