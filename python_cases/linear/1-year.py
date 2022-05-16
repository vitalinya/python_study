from math import pi

def year(r,v):
	year=2*pi*r*1000000/(v*60*60*24)
	return year

#Mercury
print('Mercury days =',year(57.909, 47.87))
#Venus
print('Venus days =',year(108.21, 35.02))
#Earth
print('Earth days =',year(149.60, 29.76))
#Mars
print('Mars days =',year(227.94, 24.13))
#Jupiter
print('Jupiter days =',year(778.41, 13.07))
#Saturn
print('Saturn days =',year(14294, 9.67))
#Uranus
print('Uranus days =',year(28710, 6.84))
#Neptune
print('Nepture days =',year(44983, 5.48))
#Pluto
print('Pluto days =',year(59064, 4.75))
