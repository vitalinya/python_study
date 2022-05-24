from random import randint

def sum(num1,num2):
	print(num1,num2)
	if num1 == num2 or abs(num1 - num2) == 5:
		return True
	else:
		return False

num1 = randint(0, 9)
num2 = randint(0, 9)

print(sum(num1,num2))