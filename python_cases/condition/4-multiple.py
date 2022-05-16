from random import randint

number1 = randint(-100, 100)
number2 = randint(-100, 100)

print('number1 =',number1,'number2 =',number2)

if number1 % number2 == 0:
	print ('multiple')
else:
	print ('not multiple')