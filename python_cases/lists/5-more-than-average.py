from random import randint

list = [randint(0,1000) for x in range(10)]

print (list)

average = [x for x in list if x > sum(list)/len(list)]

print (sum(list)/len(list))
print (average)
