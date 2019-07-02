# filter



def greater_than_10(num): return num > 10


list = [2, 3, 44, 15, 6, 64]
print filter(greater_than_10, list)


def begins_with_e(text, prefix='e'):
    return text[0] == prefix


words = ['earth', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
print filter(begins_with_e, words)
# reduce
numbers = range(11)
print numbers
for n in numbers:
    n

square = lambda num: pow(num, 2)
for n in numbers:
    print 'number=', n, 'its square =', square(n)
'''map here makes the list of derived list to be formed'''
print map(square, numbers)
print map(str, numbers)
print [str(nu) for nu in numbers]

add_two_numbers = lambda x: x + 2
print [add_two_numbers(n) for n in numbers]




