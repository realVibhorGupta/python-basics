

a = [-2, 3.5, 4, 58, -6, 24]
print a[1]
a[0] = -34
print a  # lists are mutable
for s in a:
    print s

b = ["banana", "apple "]
c = a + b
print c

stuff = list()
stuff.append("book")

stuff.append(00)
print stuff

print 15 in stuff
print 16 not in stuff

print a.sort()
print range(len(a))

print range(5)

print max(stuff)

# numlist = list()
# while True:
#     inp = raw_input("Enter the  number :")
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist) / len(numlist)
# print "Avg : ", average

abc = "with three words"

stuff = abc.split()
print stuff

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i