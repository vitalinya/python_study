from random import randint
list = []
for item in range(10):
	number = randint(0, 100)
	list.append(number)
print (list)

print (min(list))
print (max(list))
