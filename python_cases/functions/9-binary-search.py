from random import randint

list = [randint(0, 100) for x in range(21)]
number = list[randint(0, len(list))]

def binary_search(list,number):

	list.sort()
	print (list)
	print ('number =',number)

	left = 0
	right = len(list)
	middle = round(len(list)/2)

	print('left =',left,'middle =',middle,'right =',right)

	while True:
		if number > list[middle]:
			left = middle
			middle = round((left + right)/2)
			print('left =',left,'middle =',middle,'right =',right)
		elif number < list[middle]:
			right = middle
			middle = round((left + right)/2)
			print('left =',left,'middle =',middle,'right =',right)
		elif number == list[middle]:
			return middle
			break

print ('index =',binary_search(list,number))