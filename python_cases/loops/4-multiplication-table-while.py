i = 1
j = 1

while i < 11:
	while j < 11:
		print (i*j, end=' ')
		if j == 10:
			print ()
		j += 1
	j = 1
	i += 1

