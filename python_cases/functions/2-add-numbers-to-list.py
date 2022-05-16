from random import randint

number1 = randint(0, 100)
number2 = randint(0, 100)

list = []
number = 10

def fill_list(list,num):
	for item in range(num):
		list.append(randint(0,10))

fill_list(list, number)

print (list)
