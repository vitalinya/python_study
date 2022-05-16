from random import randint

a = randint(1,100)
b = randint(1,100)
c = randint(1,100)

print (a,b,c)

if a + b > c and a + c > b and b + c > a:
	print('triangle can exist')
else:
	print ('triangle cannot exist')