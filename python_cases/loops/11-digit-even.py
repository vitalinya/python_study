from random import randint

number = randint(0,100000)

print(number)

divider1 = 10
divider2 = 1
buffer = 0
even = 0
noteven = 0
while number // divider2 > 0:
	digit = int((number % divider1 - buffer)/divider2)
	buffer = number % divider1
	divider1 *= 10
	divider2 *= 10
	if digit % 2 == 0:
		even += 1
	elif digit % 2 == 1:
		noteven += 1

print ('even =',even,'not even =',noteven)