from random import randint

def distance(x1,y1,x2,y2):
	print(x1,x2,y1,y2)
	return ((x1-x2)**2+(y1-y2)**2)**0.5

x1= randint(-9, 9)
x2= randint(-9, 9)
y1= randint(-9, 9)
y2= randint(-9, 9)

print(distance(x1, y1, x2, y2))