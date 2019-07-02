def hello():
    print "hello"
    print "hello"
    print "fun"


hello()
hello()
print "Zip"
hello()


def add(a, b):
    print a + b


big = max("hello world")
tiny = min("hello world")

print big

print tiny

add(2, 3)

print float(99) / 100
i = 32
print type(i)
f = float(i)
print f

print type(f)

x = 5
print "hello1"


def print_lyrics():
    print "i am a lumber jack "
    print "i sleep at night"


print "yo"
print_lyrics()
x += 5
print x


def greet(lang):
    if lang == 'es':
        print "Hola"
    elif lang == "fr":
        print "Bonjour"
    else:
        print "Hello"


greet('es')
greet('fr')
greet('h')


def greet():
    return "hello"


print greet(), "vibhor"
print greet(), "nikhil"


def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return 'Hello'


print greet('en'), "vibhor"
print greet('es'), "rahul"
print greet('fr'), "ritu"


# function overloading
def addtwo(a, b):
    added = a + b
    return b


x = addtwo(2, 7)
print x


def function1():
    print "hello first function"


def function2(a):
    a = 2
    print "the value of a  = ", a


def function(a, b):
    print "the sum of two nu8mbers are ", a + b


function1()
function2(3)
function(2, 3)


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 66, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
