from Strings import word

purse = dict()
purse['money'] = 16
purse['candy'] = 4
purse['tissues'] = 15
print purse

print purse['candy']
purse['candy'] += 5
print purse['candy']
print purse

dicts = dict()
dicts['age'] = 21
dicts['course'] = 182
print dicts

dicts['age'] = 232
print dicts

jjj = {'chuck': 1, "fred": 2, "vasu": 3}
print jjj
aaa = {}
print aaa

place = {}

numbers = [2, 5, 3, 12, 5, 66, 5, 22]

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print ccc
ccc['cwen'] += 1
print ccc

counts = dict()
names = ['vibhor', 'vatsal', 'rahul ', 'nirmal ', 'vibhor']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

print counts

counts = dict()
names = ['vibhor', 'vatrtsal', 'rahul ', 'nirmal ', 'vibhor']
for name in names:
    counts[name] = counts.get(name, 1) + 1

print counts

counts = dict()
print "enter a line of text :"
# line = raw_input('')

# words = line.split()
# print "words : ", words


print "Counting ..."

# for word in words:
#   counts[word] = counts.get(word, 0) + 1

print 'Counts : ', counts

counts = {'chuck ': 1, 'fred': 32, 'jan': 34}
for key in counts:
    print key, counts[key]

print counts.keys()
print counts.values()
print counts.items()

stuff1 = dict()
print stuff1.get('candy', -1)
