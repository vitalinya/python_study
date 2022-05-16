from random import randint

measure = ['celsium','farenheit']
choose_measure = measure[randint(0, 1)]

if choose_measure == 'celsium':
	temperature = randint(-273, 100)
	temperature_convert = temperature*9/5 + 32
elif choose_measure == 'farenheit':
	temperature = randint(-479, 100)
	temperature_convert = (temperature - 32)*5/9

print (choose_measure)
print (temperature)
print (temperature_convert)