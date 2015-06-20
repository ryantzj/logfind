from sys import argv
import re

script, filename, keyword = argv
names = keyword
print(sys.argv)
p = re.compile(names,re.I)
print "%r" % names


with open(filename) as f:
    for line in f:
		print "%r" % line
	        m =	p.findall(line)
		print(m)
print "Here's your file %r:" % filename
print "keyword is:", keyword
