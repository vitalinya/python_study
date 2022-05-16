import re

text = '''Hi! My name Vitaly.
Currently i'm studying python languange,
work on exersices and work hardly.'''

signs = ['!','.',',']

list = text.split()

for item in range(len(list)):
	if list[item][-1] in signs:
		list[item] = list[item][:-1]

print (list)