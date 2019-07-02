a = 'hello world'
try:
    b = int(a)
except:
    b = -1

print "First", b

a = '123'
try:
    b = int(a)
except:
    b = -1
print 'second', b

rawstr = raw_input('enter a number:')

try:
    a = int(rawstr)
except:
    a = -1

if a > 0:
    print 'nice work'
else:
    print 'not a number'

enter_hours = raw_input('enter hours')
enter_rate = raw_input('enter rate')

if enter_hours > 40:
    pay = 40 * enter_rate + 5 * 15

else:
    pay = 40 * enter_hours + 5
print pay
