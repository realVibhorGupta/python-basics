str1 = "hello "
str2 = "vibhor"
name3 = str1 + str2
print name3

str3 = '123'
str3 = int(str3) + 1
print str3
#
# name4 = raw_input("enter your name :")
# print name4
#
# apple = raw_input("enter the number of apples")
# x = int(apple) - 10
# print x

fruit = "banana"
letter = fruit[1]
print letter
x = 3
e = fruit[x - 1]

print e

print len(fruit)

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print index, letter
    index += 1

fruit = "banana"
a = 0
for letter in fruit:
    while a > 0:
        a += 1
        print a, letter

s = "vibhor gupta"
print s[0:4]
print s[6:9]
print s[6:60]
print s[7:]
print s[:5]

# string concatenation
a = "hello"
b = a + "there"
print b

a = "hello"
b = a + " " + "there"
print b

a = "hello "
b = a + "there"
print b

fruit = "banana"
print 'n' in fruit

print 'm' in fruit

if 'a' in fruit:
    print "found it"

word = "banana"
if word == "banana":
    print "all right , banana"

if word < "banana":
    print "your word " + word + " ,comes before banana"
elif word > "banana":
    print "your word " + word + " ,comes after banana"
else:
    print "All right  ,  banana"

# string library
greet = "   hello Vibhor   "
print greet.lower()
print greet.upper()
print greet
print greet.__len__()
print type(greet)
print greet.capitalize()
print greet.center(5, 'a')
print greet.endswith('a')
print greet.find('h')
print greet.lstrip('r')
print greet.replace('hello', 'bonjour')

fruit = "banana"
pos = fruit.find('na')
print pos
aa = fruit.find('z')
print aa
print fruit.upper()

print greet.lstrip()
print greet.rstrip()
print fruit.rsplit()

