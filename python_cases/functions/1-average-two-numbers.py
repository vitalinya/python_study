from random import randint

number1 = randint(0, 100)
number2 = randint(0, 100)

print(number1,number2)

def average(num1,num2):
	return round((num1 + num2)/2,2)

print(average(number1,number2))
