from random import randint

def check(num):
	if 10 < num < 1000:
		print ('number =', num, 'between 10 and 1000')
	elif 1000 < num < 2000:
		print ('number =', num, 'between 1000 and 2000')

check(randint(10,2000))