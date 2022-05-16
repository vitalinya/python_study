from string import ascii_letters
from random import randint

string = ''

for item in range(0,11):

	string += ascii_letters[randint(0,51)]

print (string)

lower = 0
upper = 0

for item in string:
	if item.islower():
		lower += 1
	elif item.isupper():
		upper += 1

lower_p = round(lower/len(string)*100,2)
upper_p = round(upper/len(string)*100,2)

print(lower_p,upper_p)

# print ('percent of lower = %s %' % lower_p)
# print ('percent of upper = %s %' % upper_p)