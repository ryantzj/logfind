from sys import argv
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('keyword', nargs='+')
parser.add_argument('-o',dest='rex',action='store_const',const="|",default=" ")
args = parser.parse_args()
keywords = (args.rex).join(args.keyword)
print(keywords)
p = re.compile(keywords,re.I)

with open(args.filename) as f:
	for line in f:
		m = p.findall(line)
     		print(m)
# print "Here's your file %r:" % filename
