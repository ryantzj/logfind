from sys import argv
import re

script, filename, keyword = argv
name = ["this"]

with open(filename) as f:
    for line in f:
        for line in name:
 		m = re.match("(^[a-z]+)",line)
		if m:
			print(m.groups())
print "Here's your file %r:" % filename
print "keyword is:", keyword
