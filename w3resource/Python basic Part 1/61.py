from random import randint

distance = randint(1, 10)
measures = ['yard','inch','mile']
measure = measures[randint(0, len(measures)-1)]

def convert(height,measure):
	if measure == 'yard':
		return round(distance/3,2)
	elif measure == 'inch':
		return distance*12
	elif measure == 'mile':
		return round(distance*0.000189394,5)

print(distance,measure)
print(convert(distance,measure))