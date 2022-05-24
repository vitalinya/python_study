from random import randint

height = randint(1, 10)
measures = ['feet','inch']
measure = measures[randint(0, len(measures)-1)]

def convert(height,measure):
	if measure == 'inch':
		return height*2.54
	elif measure == 'feet':
		return height*30.48

print(height,measure)
print(convert(height,measure))