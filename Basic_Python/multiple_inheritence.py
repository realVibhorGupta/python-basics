class Mario(object):
    def move(self):
        print 'i am moving'


class Mushroom(object):
    def eat(self):
        print 'i am bigger!!'


class BiggerMario(Mario, Mushroom):
    def flower(self):
        print 'now i can shoot'


bm = BiggerMario()
bm.move()
bm.eat()
bm.flower()
# this shows that python shows multiple inheritence
