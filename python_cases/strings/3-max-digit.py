from random import uniform

number = str(uniform(0,10000000))`
max = 0
for item in number:
	if item == '.':
		continue
	if max < int(item):
		max = int(item)

print(number, max)