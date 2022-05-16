from random import randint

list = [randint(0,1000) for x in range(10)]

print(list)

for item in range(10):
	number = randint(0,1000)
	print (number)
	list[item] = number
	print (list)