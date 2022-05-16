from random import randint

number1 = randint(1, 100)
number2 = randint(1, 100)

def gcd(num1,num2):

	if number1 < number2:
		divident = number2
		divider = number1
	else:
		divident = number1
		divider = number2

	while divident % divider != 0:
		buffer = divider
		divider = divident % divider
		divident = buffer

	print ('gcd =',divider)
	return divider


def lcm(num1,num2):

	return int((num1*num2)/gcd(num1, num2))

print(number1,number2)
print('lcm =',lcm(number1,number2))