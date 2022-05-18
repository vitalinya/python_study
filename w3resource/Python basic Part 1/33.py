from random import randint

def sum(num1,num2,num3):
	print(num1,num2,num3)
	if num1 == num2 or num1 == num3 or num2 == num3:
		return 0
	else:
		return num1+num2+num3

num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)

print(sum(num1,num2,num3))