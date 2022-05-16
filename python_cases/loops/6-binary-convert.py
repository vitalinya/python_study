from random import randint

num = randint(0,100)
num_base=randint(2,9)
new_num = 0
base = 0
remainder = num
print (num,num_base)
multiplier = num
while multiplier > 0:
	remainder = multiplier % num_base
	multiplier = multiplier // num_base
	new_num += remainder*(10**base)
	base += 1
	print (remainder,multiplier)

print (new_num)