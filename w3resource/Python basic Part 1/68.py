from random import randint

def count(number):
	sum = 0
	print(number)
	for s in str(number):
		sum += int(s)
	return sum

number = randint(1000, 9999)

print(count(number))

