import sys

from getting_started import b

fruits = ["apple ", "banana ", "orange ", "guava", "pineapple ", "cucumber "]
for fruit in fruits:
    if fruit[0] in "aeiou":
        print (fruit + "starts with a vowel")

vowel_names = []
for name in fruits:
    if name[0] in "aeiou":
        vowel_names.append(name)
print vowel_names

prices = [2, 34, 5, 2.325, 325.4, 542, 52, 54]
total = 0
for cost in prices:
    total = total + cost
print total
print sum(prices)

# print all words in scrabble
print 'hello{0}'.format(str(6))


def main():
    """

    :rtype: object
    """
    print sys.argv


if __name__ == '__main__':
    main()
name = "vibhor"
print name.find("h")

a = "Hello"
print a[1:3]
print a[2:5]
print a[:]
print a[:4]
print a[2:]

a = [2, 4, 5, 'vibhor']
print a
b = []
b = a[:]
print b

a = [1, 4, 2, 8986, 12, 66, -4213, 6]
print a

print sorted(a)
print sorted(a, reverse=True)
a = ['afaaaa', 'hfdhzzzfdhhzfh', 'cafdhfarrrrafdh', 'zafhbbaha', 'xhfdfc', 'qadfhddddddd']
print a
print sorted(a)
print sorted(a, reverse=True)

print sorted(a, key=len)
print sorted(a)
# print sorted(a, key=name)
print ':'.join(a)
b = '\\'.join(a)
print b
print ':'.split(b)

result = []
for s in b: result.append(s)
print result

print range(20)
print (1, 2, 3)

a = [(1, 'q'), (2, 'b'), (1, 'c')]
print a
print sorted(a)
(x, y) = (1, 2)
print (x, y)
print x
print y

dict = {}
print dict
dict['a'] = 'alpha'
dict['o'] = 'omega'
dict['g'] = 'gamma'

print dict['a']
print dict.get('x')
print dict.get('o')

print 'a' in dict
print 'b' in dict
print 'o' in dict
print dict.keys()

# print dict.popitem()
print dict.viewvalues()
print dict.items()

for k in sorted(dict.keys()): print 'key : ', k, '->', dict[k]

for tuple in dict :print tuple