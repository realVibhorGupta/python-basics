n = 5
while n > 0:
    print n
    n -= 1

print "bye byue!!"
print n

n = 4
while n > 0:
    print "vibhor"
    print "goes on"
    n -= 1

print "dry off"

n = 0
while n > 0:
    print "hello"
    print "vibhor"
print "loop doesnot worked"
#
# while True:
#     line = raw_input('>')
#     if line == 'done':
#         break
#     print line
# print "Done"
#
# while True:
#     line = raw_input('>')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print line
# print "Done"


for i in [5, 4, 3, 2, 1]:
    print  i
print "bbeye"

friends = ['joseph', 'glen', 'sally']

for friend in friends:
    print friend
print "nice to meet you all!"
counter = 0
likes = 0
sum = 0
number = 0

#average of numbers
#    in a list
print "Before"
for s in [2.4, 4, 22, 2, 2, 4, 3, 5234, 213]:
    counter = counter + s
    sum = sum + s
    likes += 1
    number += 1

print "after", counter
print "likes", likes
print "sum", sum
print "average", sum / number

# filtering  numbers
print  "before"
for value in [2.4, 4, 22, 2, 2, 4, 3, 5234, 213]:
    if value > 20:
        print "larger number : ", value
print  "after"

"""boolean values"""

found = False
print "before :", found
for value in [32, 25, 234, 66, 4, 2, 12, 3]:
    if value == 3:
        found = True
        break
    print found, value
print "after :", found



#smallest number in a list
smallest = None
print "before ", smallest
for value in [32, 25, 234, 66, 4, 2, 12, 3]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print smallest, value
print "after", smallest


