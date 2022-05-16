from random import randint

calc_parameter = ['weight','volume','density']

choosed_parameter = calc_parameter[randint(0, 2)]

weight = randint(0, 10000)
volume = randint(0, 10000)
density = randint(0, 10000)

if choosed_parameter == 'weight':
	calc_weight = volume*density
	print('calculate weight =',calc_weight,'volume =',volume,'density =',density)
elif choosed_parameter == 'volume':
	calc_volume = weight/density
	print('calculate volume =',calc_volume,'weight =',weight,'density =',density)
elif choosed_parameter == 'density':
	calc_density = weight/volume
	print('calculate density =',calc_density,'weight =',weight,'volume =',volume)
