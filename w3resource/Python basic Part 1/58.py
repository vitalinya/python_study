from random import randint
def sum(list,i=0,summ=0):
	if i == len(list)-1:
		print(summ,i)
		return summ
	elif list[i] >= 0:
		print(summ,i)
		return sum(list,i+1,summ+list[i])
	elif list[i] < 0:
		print(summ,i)
		return sum(list,i+1,summ)

list = [randint(-9, 9) for x in range(10)]
print (list)
print(sum(list))