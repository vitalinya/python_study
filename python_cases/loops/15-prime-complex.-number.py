from random import randint

number = randint(1, 1000)

print (number)
for divider in range (2,number):
	if number % divider == 0:
		print ('number is complex, divider =', divider)
		break
else:
	print ('number is simple')

