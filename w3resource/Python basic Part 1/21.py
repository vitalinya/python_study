from random import randint

def even_odd(num):
	print(num)
	if num % 2 == 0:
		print('even')
	else:
		print('odd')

even_odd(randint(0, 100))