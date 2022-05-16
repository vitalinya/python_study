from random import randint

number = randint(0,10000)

print(number)

reverse = 0
divider1 = 10
divider2 = 1
buffer = 0
summ = 0
multiple = 1
while number // divider2 > 0:
	digit = int((number % divider1 - buffer)/divider2)
	reverse = reverse*10 + digit
	print (digit)
	buffer = number % divider1
	divider1 *= 10
	divider2 *= 10


print ('reverse =',reverse)
