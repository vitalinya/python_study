from random import randint

list = [randint(0,1000) for x in range(10)]

check = [x for x in list if x > 100 and x < 500 ]

print (list)
print (check)
print (len(check))