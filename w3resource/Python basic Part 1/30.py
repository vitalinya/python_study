from random import randint

def triangle(base,height):
	return base,height,0.5*base*height

base = randint(0, 9)
height = randint(0, 9)

print(triangle(base, height))