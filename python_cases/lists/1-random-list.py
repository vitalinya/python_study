from random import randint
list = []
for item in range(10):
	number = randint(0, 100)
	print (number)
	list.append(number)

print(list)