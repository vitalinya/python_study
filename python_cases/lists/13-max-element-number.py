from random import randint

list = [randint(0, 100) for x in range(30)]

max = 0
element = 0

for item in range(len(list)):
	if max < list.count(list[item]):
		max = list.count(list[item])
		element = list[item]

print (list)

print (element,max)