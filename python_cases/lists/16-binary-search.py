from random import randint

list = [randint(0, 100) for x in range(21)]
print (list)
list.sort()
print (list)

left = 0
right = len(list)
middle = round(len(list)/2)

print (left,middle,right)

number = list[randint(0, len(list))]

print (number)

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
		print('index =',middle)
		break