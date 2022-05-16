from random import randint

def random_sum():
	number = randint(100,999)
	print (number)
	num1 = number // 100
	num2 = number // 10 % 10
	num3 = number % 10
	sum = num1 + num2 + num3
	return print(sum)
random_sum()