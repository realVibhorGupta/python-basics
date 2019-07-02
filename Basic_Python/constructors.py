class PartyAnimal:
    def __init__(self, nam):
        self.name = nam
        print self.name, "i am  constructed"

    x = 0

    def party(self):
        self.x += 1
        print self.name, "party count ", self.x


s = PartyAnimal('VIbhor')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
