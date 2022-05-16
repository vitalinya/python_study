def isstring(string):
	if string[0:1] == 'Is':
		print(string)
		return string
	else:
		return 'Is' + string

print(isstring('Isakov'))
print(isstring('Smirnov'))
