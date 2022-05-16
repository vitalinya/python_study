from random import randint

number = randint(0, 100)
guess_number = randint(0,100)
iter = 0
while guess_number != number:
	guess_number = randint(0,100)
	iter += 1
else:
	print ('iter =', iter)
	print ('Guess match, origin number =', number)


