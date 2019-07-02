class pet:
    number_of_legs = 0

    def sleep(self):
        print "zzzzzzzz "

    def count_legs(self):
        print "i have %s legs" % self.number_of_legs


doug = pet()
doug.number_of_legs = 4

print "Doug Has %s legs " % doug.number_of_legs

doug.sleep()
doug.count_legs()

nemo = pet()
nemo.number_of_legs = 0
nemo.count_legs()


# inheritence in python

# single inheritence

class dog(pet):
    def __init__(self):
        pass

    def bark(self):
        print "woof"


doug = dog()
doug.bark()
doug.sleep()
doug.number_of_legs = 4
doug.count_legs()


class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print "so far ", self.x


an = PartyAnimal()
an.party()
an.party()
an.party()


