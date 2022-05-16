from random import randint

list = [randint(0,1000) for x in range(10)]

print (list)

even = [x for x in list if x % 2 == 0]

print (even)
print (len(even))

noteven = [x for x in list if x % 2 == 1]

print (noteven)
print (len(noteven))