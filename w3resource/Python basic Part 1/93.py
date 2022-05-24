from random import randint

num1 = num2 = [randint(0,9) for x in range(10)]

num3 = num4 = randint(0,9)

num5 = num6 = [str(randint(0,9)) for x in range(10)]

print (num1,num3,num5)

print (type(num1))
print (type(num3))
print (type(num5))

print (num1 is num2)
print (num3 is num4)
print (num5 is num6)
