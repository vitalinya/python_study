import string
from random import randint
letter = (string.ascii_lowercase[randint(0, len(string.ascii_lowercase)-1)])
vowels = 'aeijouz'

def vowels_check(letter):

	if letter in vowels:
		return letter + ' ' + 'is vowel'
	else:
		return letter + ' ' + 'isn\'t vowel'

print(vowels_check(letter))
