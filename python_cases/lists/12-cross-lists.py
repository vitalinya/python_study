from random import randint

list1 = [randint(0, 100) for x in range(10)]
list2 = [randint(0, 100) for x in range(20)]

print (list1)
print (list2)

list3 = []

for item in range(len(list1)):
	if list1[item] in list2:
		list3.append(list1[item])

print (list3)
