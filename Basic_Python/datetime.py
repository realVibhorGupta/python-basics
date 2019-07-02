import calendar
import time

ticks = time.time()
print 'number of ticks since 12:00am, march 1, 2016:', ticks

localtime = time.localtime(time.time())
print 'current local time is : ', localtime

localtime = time.asctime(time.localtime(time.time()))
print 'Local current time :', localtime

cal = calendar.month(2016, 12)
print "Here is the calendar:"
print cal