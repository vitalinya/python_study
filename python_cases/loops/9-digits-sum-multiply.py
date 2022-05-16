from random import randint

number = randint(0,99)

print(number)


divider1 = 10
divider2 = 1
buffer = 0
summ = 0
multiple = 1
while number // divider2 > 0:
	digit = int((number % divider1 - buffer)/divider2)
	buffer = number % divider1
	divider1 *= 10
	divider2 *= 10
	summ += digit
	multiple *= digit

print ('sum =',summ,'multiple =',multiple)