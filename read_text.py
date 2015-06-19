from sys import argv
import re

script, filename, keyword = argv
p = re.compile(r'(?P<word>\b\w+\b)')

with open(filename) as f:
    for line in f:
        result = p.search(line)
        print "search found %r:" % result.group('word')

print "Here's your file %r:" % filename
print "keyword is:", keyword
