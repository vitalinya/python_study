from random import randint

list = [randint(0, 9) for x in range(10)]
directions = ['left','right']
direction = directions[randint(0, len(directions)-1)]
step = randint(0, len(list)-1)

def cycle_shift(list,step,direction):
	print(list)
	print(step)
	print(direction)
	for i in range(step):
		left = list[0]
		right = list[-1]
		if direction == 'right':
			list.pop(-1)
			list = [right] + list
		elif direction == 'left':
			list.pop(0)
			list = list + [left]

	return list

print(cycle_shift(list, step, direction))




