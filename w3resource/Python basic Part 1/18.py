from random import randint

def check(num1,num2,num3):
	print(num1,num2,num3)
	if num1 == num2 == num3:
		return (num1+num2+num3)*3
	else:
		return num1+num2+num3

print(check(randint(0,3),randint(0,3),randint(0,3)))