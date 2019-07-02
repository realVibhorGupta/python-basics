x = ('glenn', 'silly ', 'joseph')
print x[1]

y = {1, 2, 3}
print y
print max(y)

for iter in y:
    print iter

# x[2] = 6

x = (3, 1, -1)
x, y = (3, 4)
print x, y

d = dict()
d["vibhor"] = 2
d["nirmal "] = 4

for (k, v) in d.items():
    print k, v

tup = d.items()
print tup

print  (1, 2, 4) < (4, 5, 6)
print ('jones', 'sally') < ('adams', 'fered')

d = {'a': 10, "c": 40, "b": 30}
t = d.items()
print t

t.sort()
print t
print dir(x)
print "sorted order :", sorted(d.items())
temp = list()
for k, v in d.items():
    temp.append((v, k))
print temp

fhand = open('C:\\Users\\vibhor\\Desktop\\New folder\\c++headerfiles.txt', 'r')
counts = dict()
for lines in fhand:
    words = lines.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for key, val in counts.items():
    lst.append((val, key))
print lst
lst.sort(reverse=True)
for val, key in lst[:10]:
    print key, val

c = {'a': 10, 'b ': 2, 'c': 33}
print sorted([(v, k) for k, v in c.items()])



