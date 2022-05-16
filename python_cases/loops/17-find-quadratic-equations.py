from random import randint

for a in range(-10,10):
	for b in range(-10,10):
		for c in range(-10,10):
			if a == 0 or b == 0 or c ==0:
				continue

			D = b**2 - 4*a*c

			x1 = (-b + D**0.5)/(2*a)
			x2 = (-b - D**0.5)/(2*a)

			if x1*x2 == c and x1+x2 == -b:
				print ('x1 =',x1,'x2 =',x2)
				print ('%sx^2 + %sx + %s' % (a,b,c))
