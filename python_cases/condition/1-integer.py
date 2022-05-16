from random import randint

number = randint(-100, 100)
print(number)
if number > 0:
	print('positive')
elif number <0:
	print('negative')