def isstring(string):
	if string[0:2] == 'Is':
		return string
	else:
		return 'Is' + string

print(isstring('Isakov'))
print(isstring('Smirnov'))
