from random import randint

list = [randint(0, 100) for x in range(10)]
print (list)
for count in range(1,len(list)-1):
	for item in range(0,len(list)-1):
		if list[item] > list[item+1]:
			list[item+1],list[item] = list[item],list[item+1]
		else:
			continue

print(list)