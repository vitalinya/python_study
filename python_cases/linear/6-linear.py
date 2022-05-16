from random import randint

x1 = randint(1,9)
y1 = randint(1,9)
x2 = randint(1,9)
y2 = randint(1,9)
print ('x1 =',x1,'y1 =',y1,'x2 =',x2,'y2 =',y2)
k = (y1 - y2)/(x1 - x2)
print ('k=',k)
b = y1 - k*x1
print ('b=',b)

print ('y = %sx + %s' % (k, b))