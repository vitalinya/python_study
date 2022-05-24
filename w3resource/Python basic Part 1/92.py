from string import punctuation

print (punctuation)

string = 'P@ssw0rd'

for item in string:
	if item in punctuation:
		print('In string present special symbol =',item)

