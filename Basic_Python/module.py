import math
import random
import string
import this
import time
from Tix import Tk

import sys

print dir(math)
print math.__name__, math.__doc__
words = "hello world how are you "
print words.split()
print string.split(words)

print dir(random)

print random.randint(1, 9)
print dir(time)

print time.asctime()
print time.gmtime(20)
print time.timezone
print time.time()

window = Tk()#this will make  a prompt window
window.mainloop()

print sys.argv

