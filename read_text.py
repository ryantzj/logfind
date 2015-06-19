from sys import argv
import re

script, filename, keyword = argv
with open(filename) as f:
    for line in f:
        result = re.search('is',line)
        print "search found %r:" % result

print "Here's your file %r:" % filename
print "keyword is:", keyword
