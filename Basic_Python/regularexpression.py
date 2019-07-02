import re

hand = open('C:\\Users\\vibhor\\Desktop\\New folder\\c++headerfiles.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^This ', line):
        print line
