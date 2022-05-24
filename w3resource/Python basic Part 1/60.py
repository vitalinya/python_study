from random import randint
leg1 = randint(1, 10)
leg2 = randint(1, 10)
def hipotenuse(leg1,leg2):
	print (leg1,leg2)
	return (leg1**2 + leg2**2)**0.5

print(hipotenuse(leg1, leg2))