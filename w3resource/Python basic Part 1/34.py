from random import randint

def sum(num1,num2):
	print(num1,num2)
	if 15 < num1+num2 < 20:
		return 20
	else:
		return num1+num2

num1 = randint(0, 9)
num2 = randint(0, 9)

print(sum(num1,num2))