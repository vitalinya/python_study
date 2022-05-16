from random import randint

number = str(randint(0,10000))

sum = 0

for item in number:
	digit = int(item)
	sum += digit

print (number,sum)

