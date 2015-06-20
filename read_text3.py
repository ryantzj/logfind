from sys import argv
import re

script, filename, keyword, keyword2 = argv
names = keyword+"|"+keyword2
p = re.compile(names,re.I)


with open(filename) as f:
    for line in f:
	print(line)
        m =	p.findall(line)
	print(m)
print "Here's your file %r:" % filename
