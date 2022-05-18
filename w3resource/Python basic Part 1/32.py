from random import randint

def gcd(divide,divider):
	print(divide,divider)
	while divide % divider != 0:
		remain = divide % divider
		divide = divider
		divider = remain
		print('divide =',divide,'divider =',divider)
	return divider

num1 = randint(1, 100)
num2 = randint(1, 100)

print('lcd = ',int(num1*num2/gcd(num1,num2)))