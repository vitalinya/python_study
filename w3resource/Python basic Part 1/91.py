from random import randint

x = randint(0, 9)
y = randint(0, 9)

print (x,y)

x,y = y,x

print (x,y)