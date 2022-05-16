from random import randint

year = randint(1970, 2022)

print (year)

if year % 4 == 0:
	print ('This year is leap')
else:
	print ('This year not leap')