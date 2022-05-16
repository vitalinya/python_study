from random import randint

factorial = randint(0, 5)
print (factorial)
result = 1
for number in range(1,factorial+1):
	result *= number

print (result)