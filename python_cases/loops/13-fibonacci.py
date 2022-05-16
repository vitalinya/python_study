from random import randint

N = randint(0, 10)

print (N)
for number in range(N):
	if number == 0:
		fibonacci0 = fibonacci = 0
	elif number == 1:
		fibonacci1 = fibonacci = 1
	else:
		fibonacci = fibonacci0 + fibonacci1
		fibonacci0 = fibonacci1 
		fibonacci1 = fibonacci
	print (fibonacci, end=' ') 

