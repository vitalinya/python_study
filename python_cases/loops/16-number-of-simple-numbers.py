from random import randint

simple = 0

for iter in range(10):
	number = randint(1, 1000)
	print (number, iter)
	for divider in range (2,number):
		if number % divider == 0:
			print ('number is complex, divider =', divider)
			break
	else:
		print ('number is simple')
		simple += 1

print ('number of simple =',simple)

