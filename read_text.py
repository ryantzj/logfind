from sys import argv
import re

script, filename, keyword = argv
pattern = ['this','that']
regex = re.compile("f\(\s*([^,]+)\s*,\s*([^,]+)\s*\)")
with open(filename) as f:
    for line in f:
        result = regex.search(pattern,line)
        print "search found %r:" % result

print "Here's your file %r:" % filename
print "keyword is:", keyword
