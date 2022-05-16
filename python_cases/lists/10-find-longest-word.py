string = 'I have the best and smartest kids in the world'

list = string.split(' ')

max = 0

for item in range(len(list)-1):
	if max < len(list[item]):
		max = len(list[item])
		max_word = list[item]

print (max_word)

