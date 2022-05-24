def check(num1,num2):
	print(num1,num2)
	if type(num1) == int and type(num2) == int:
		return num1+num2
	else:
		return False

num1 = 1
num2 = 2

print(check(num1, num2))