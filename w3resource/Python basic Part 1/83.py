from random import randint

list = [randint(0, 20) for x in range(5)]

number = randint(0, 20)

def greater(list,number):
	print(list,number)
	for item in range(number):
		if item in list:
			return False
			break
	else:
		return True

print(greater(list, number))
