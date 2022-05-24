from random import randint

types = ['list','tuple','set','dict']

data_type = types[randint(0, len(types)-1)]

print (data_type)

data_list = [randint(0, 9) for x in range(3)]

print(data_list)

def summ(container):
	if type(container) == list:
		return sum(container)
	elif type(container) == tuple:
		return sum(list(container))
	elif type(container) == set:
		return sum(list(container))
	elif type(container) == dict:
		return sum(list(container.values()))

if data_type == 'tuple':
	data_tuple = tuple(data_list)
	print(data_tuple,type(data_tuple))
	print(summ(data_tuple))
elif data_type == 'set':
	data_set = set(data_list)
	print(data_set)
	print(data_set,type(data_set))
	print(summ(data_set))
elif data_type == 'dict':
	data_dict = dict(zip(range(len(data_list)),data_list))
	print(data_dict)
	print(data_dict,type(data_dict))
	print(summ(data_dict))
elif data_type == 'list':
	print(data_list,type(data_list))
	summ(data_list)