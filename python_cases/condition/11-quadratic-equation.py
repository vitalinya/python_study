from random import randint

a = randint(-10, 10)
b = randint(-10, 10)
c = randint(-10, 10)

print ('%sx^2 + %sx + %s' % (a,b,c))

D = b**2 - 4*a*c

x1 = (-b + D**0.5)/(2*a)
x2 = (-b - D**0.5)/(2*a)

if x1*x2 == c and x1+x2 == -b:
	print ('x1 =',x1,'x2 =',x2)
