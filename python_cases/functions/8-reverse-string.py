from string import ascii_letters
from random import randint

string = ''

for item in range(0,11):

	string += ascii_letters[randint(0,51)]

def reverse(string):
	return string[len(string)::-1]

print (string,'<=>',reverse(string))