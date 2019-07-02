

print "hello" + str(1)

print len("name")

print "A" * 20

h = " happy "
b = " birthday "

print ((h + b) * 10)

print (3 ** 3)
print type(False)

print 0 == 0

print 0 != 1

print "A" == "a"

print 2 <= 3

print "H" in "Hello"

print "a" not in "abcjsldhg"

print "a" not in "1233"

if 4 > 3:
    print ("4 is greater than 3")
if 4 > 13:
    print ("4 is greater than 3")

if "banana" in "bananajhwqgug":
    print ("hello it is banana")

sister = 12
brother = 15

if sister > brother:
    print ("sister is older ")
else:
    print ("brother is older")

print 0 < 1 and 22 < 44
print 4.3 < 23 and 933.4 < 445
print 344 > 34 or 34 < 553
print "a" in "abc" and "b" in "abc" and "c" in "abc "
if 23 > 2 and 34 < 55:
    print ('you got it!')

priya = 14
vibhor = 14

if priya < vibhor:
    print ("vibhor is older")
elif priya == vibhor:
    print ("both are of same age")
else:
    print ("priya is older than vibhor")

name = " VIBHOR "
print name.lower()

name1 = "gupta"
print name1.upper()

print len(name)

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

first_name = "vibhor"
last_name = "gupta"
print "My first name is %s  and my Last name is %s" % (first_name, last_name)
"""
name = raw_input("what is your name")
age = raw_input("what is your age")
place = raw_input("where are you from? ")

print "Ah so you are %s , you are %s years old and you are from %s " % (name, age, place)"""

your_list = ["a", "b", "c", "34", "3.4"]
print your_list
print type(your_list)
print len(your_list)
print "a" in your_list
print your_list[0]
your_list.append("s")

# print your_list.insert(34)
# print your_list.remove("s")
# print your_list.sort()
# print your_list.reverse()
her_list = []
print len(her_list)

names = ["hello", "bye ", " vibhor"]
names[0] = "vatsal "
print names

names.append("ksheerja")
print names
names.extend("ritu,ishant")
print names
print names.pop()
print names

print names[-1]

fruits = ["apple", "orange", "banana"]
print fruits[2:3]
print fruits
print fruits[2:]

for fruit in fruits:
    print fruit
for x in fruits:
    print x
for fruit in fruits:
    print ("i love " + fruit)
