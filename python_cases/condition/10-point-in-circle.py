from random import randint

r = randint(0, 100)
x = randint(-200, 200)
y = randint(-200, 200)

print (x, y)

r1 = (x**2 + y**2)**0.5

print (r, r1)

if r1 <= r:
	print('Point in circle')
else:
	print('Point not in circle')