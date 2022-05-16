from random import randint

number1 = randint(-100, 100)
number2 = randint(-100, 100)
number3 = randint(-100, 100)
print('number1 =',number1,'number2 =',number2,'number3 =',number3)
max = number1

if max < number2:
	max = number2

if max < number3:
	max = number3

print (max)