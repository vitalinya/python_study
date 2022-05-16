from random import randint

number = randint(10, 500)

print (number)

list = [x for x in range(2,number)]

prime_list = [2,3,5,7]

for item in range(len(list)):
	if list[item] % 2 != 0 and list[item] % 3 != 0 and list[item] % 5 != 0 and list[item] % 7 != 0:
		prime_list.append(list[item])
print (prime_list)
prime = True
for item in range(len(prime_list)):
	if number % prime_list[item] == 0:
		print('number is complex')
		prime = False
		break

if prime:
	print('number is prime')
