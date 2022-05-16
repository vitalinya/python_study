from random import randint

number = randint(10, 50)

print (number)

def isprime(number):
	prime_list = [2,3,5,7]

	for item in range(10,number):
		if item % 2 != 0 and item % 3 != 0 and item % 5 != 0 and item % 7 != 0:
			prime_list.append(item)
	prime = True
	for item in prime_list:
		if number % item == 0:
			return 'number is complex'
			prime = False
			break

	if prime:
		return 'number is prime'

print (isprime(number))


