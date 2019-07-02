import random

print "hello World"


class Person:
    def __init__(self, name):
        self.greeting = '<div>hello{name}</div>'
        self.name = name

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        self.greeting = 'HEllo{name}'
        return self.greeting.format(name=self.name)


def main():
    people = [
        dict(name=' vibhor ')
    ]
    person = random.choice(people)
    print (person)


if __name__ == '__main__':
    main()

