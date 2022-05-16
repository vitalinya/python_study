from random import randint

number = randint(-100, 100)
print(number)
if number % 2 == 0:
	print('even')
elif number % 2 != 0:
	print('not even')