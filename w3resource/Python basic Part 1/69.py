from random import randint

num1 = randint(0, 9)
num2 = randint(0, 9)
num3 = randint(0, 9)

print(num1,num2,num3)

min = min(num1,num2,num3)
max = max(num1,num2,num3)
mid = num1 + num2 + num3 - min - max

print (min,mid,max)
