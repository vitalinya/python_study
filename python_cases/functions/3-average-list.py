from random import randint

list = [randint(0,9) for x in range(0,10)]

print (list)

def list_average(list):
	print (sum(list)/len(list))

list_average(list)
