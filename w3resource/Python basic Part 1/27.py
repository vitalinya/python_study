from random import randint

def concat(list):
	print(list)
	string = ''
	for i in list:
		string += str(i)
	return string


list = [randint(0, 9) for x in range(10)]

print(concat(list))