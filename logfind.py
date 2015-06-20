from sys import argv
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('keyword', nargs='+')
args = parser.parse_args()
keywords = ' '.join(args.keyword)
print(keywords)
p = re.compile(keywords,re.I)

with open(args.filename) as f:
	for line in f:
		print(line)
		m = p.findall(line)
     		print(m)
# print "Here's your file %r:" % filename
