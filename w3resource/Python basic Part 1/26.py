from random import randint

def histogram(list):
	print(list)
	for i in list:
		print (i*'@')

list = [randint(0, 9) for x in range(10)]

histogram(list)