from random import randint

number = randint(0, 1000000000)

print(number)

divider = 10
digit = 1
while number // divider > 0:
	divider *= 10
	digit += 1

print (digit)