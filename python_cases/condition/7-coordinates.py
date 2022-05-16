from random import randint

x = randint(-100, 100)
y = randint(-100, 100)

print (x,y)

coordinates = [x>0,y>0]

if coordinates == [True,True]:
	print('first quarter')
elif coordinates == [True,False]:
	print('second quarter')
elif coordinates == [False,False]:
	print('third quarter')
elif coordinates == [False,True]:
	print('forth quarter')