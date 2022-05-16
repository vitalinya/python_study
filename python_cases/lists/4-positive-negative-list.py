from random import randint

list = [randint(-1000,1000) for x in range(10)]

print (list)

positive = [x for x in list if x > 0]

print (positive)

negative = [x for x in list if x < 0]

print (negative)