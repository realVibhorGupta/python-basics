xfile = open('C:\\Users\\vibhor\\Desktop\\New folder\\myFile.txt', 'r')
print xfile
# line counting program
count = 0
for line in xfile:
    count += 1
print 'Line Count:', count

data = xfile.read()
print len(data)

# for lines in file:
#     if lines.startswith('Inheritance:'):
#         print lines


xfile = open('C:\\Users\\vibhor\\Desktop\\New folder\\myFile1.txt', 'r')
for line in xfile:
    print line
xfile = open('C:\\Users\\vibhor\\Desktop\\New folder\\c++.pdf', 'r')
input = xfile.read()
print len(input)
print input[:]
# skipping with continue
fhand = open('C:\\Users\\vibhor\\Desktop\\New folder\\myFile1.txt', 'r')
for line in fhand:
    line = line.rstrip()
    # Skip uninteresting lines
    if not 'file' in line:
        continue
    print line

file = open('C:\\Users\\vibhor\\Desktop\\New folder\\myFile1.txt', 'w')

data = file.write("hello vibhor this is written by python language")
file.close()
