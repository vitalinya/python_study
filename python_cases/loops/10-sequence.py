from random import randint

number = randint(0, 10)
for n in range(number):
	N = (-1)**n*(0.5)**n
	print (N, end=' ')