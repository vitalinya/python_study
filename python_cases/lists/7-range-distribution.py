from random import randint

list = [randint(0,1000) for x in range(100)]

for item in range(0,1000,100):
	check = [x for x in list if x > item and x < item + 100 ]
	print ('range %d to %d contain %d' % (item,item + 100,len(check)))

