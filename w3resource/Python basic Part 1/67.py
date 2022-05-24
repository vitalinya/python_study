from random import randint

pressure = 101

def convert(pressure):
	return (pressure*68.9476,pressure*7.50062)

print(convert(pressure))