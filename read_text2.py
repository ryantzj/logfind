from sys import argv
import re

script, filename, keyword = argv
names = [keyword,'is','meow']
print "%r" % names

with open(filename) as f:
    for line in f:
		print "%r" % line
		for name in names:
 			m = re.match(r'\w+',line)
			if m:
				print(m.groups())
print "Here's your file %r:" % filename
print "keyword is:", keyword
