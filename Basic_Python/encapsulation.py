class Animal:
    def __init__(self):
        self.a = 12#this is public
        self.a = 34#this is private
        self.__a = 344#this is considered private, name mangled it can be accesed


class Dog(Animal):

    def display(self):
        print "hello world"


c = Dog()
print c.a
# print c._a
print c._Animal__a
#it does nothave private , public etc