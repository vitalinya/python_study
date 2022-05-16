from random import randint

list = [randint(0, 100) for x in range(10)]
print (list)
for count in range(0,len(list)-1):
	index = 0
	for item in range(0,len(list)-count):
		if list[index] < list[item]:
			index = item
		list[-count-1],list[index] = list[index],list[-count-1]
	
print(list)