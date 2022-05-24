from random import randint

x1 = randint(-9, 9)
y1 = randint(-9, 9)
x2 = randint(-9, 9)
y2 = randint(-9, 9)

x3 = abs(x1-x2)/2+x1
y3 = abs(y1-y2)/2+y1

print(x1,y1)
print(x2,y2)
print(x3,y3)