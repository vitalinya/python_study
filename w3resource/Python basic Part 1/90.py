import sys

def source():
	f = open(sys.argv[0])
	print (f.read())

source()