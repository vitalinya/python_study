from random import randint

values = [1, 5, 8, 3]

def check(num):
	if num in values:
		return str(num) + ' -> ' + str(values) + ': True'
	else:
		return str(num) + ' -> ' + str(values) + ': False'

number = randint(0, 9)

print(check(number))