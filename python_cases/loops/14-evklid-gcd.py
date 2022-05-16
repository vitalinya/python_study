from random import randint

number1 = randint(1, 1000)
number2 = randint(1, 1000)


if number1 < number2:
	divident = number2
	divider = number1
else:
	divident = number1
	divider = number2

print (divident,divider)

while divident % divider != 0:
	buffer = divider
	divider = divident % divider
	divident = buffer

print ('gcd =',divider)
