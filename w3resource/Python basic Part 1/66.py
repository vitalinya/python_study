from random import uniform,randint

def bmi(weight,height):
	return weight/height**2

weight = randint(60, 100)
height = round(uniform(1.6,2.0),1)

print(weight,height)
print(bmi(weight,height))
