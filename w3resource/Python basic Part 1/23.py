from random import randint

def restring(string,n):
	print(n)
	if len(string) > 2 or len(string) == 2:
		return n*string[0:2]
	elif len(string) < 2:
		return n*string

number = randint(0,9)

print(restring('string',number))
