def fibonacci(n):
	n0 = 0
	n1 = 1

	if n == 0:
		f = [n0]
		return f
	elif n == 1:
		f = [n0,n1]
		return f
	else:
		f = [n0,n1]
		for i in range(1,n):
			f.append(f[i] + f[i-1])
		return f

print(fibonacci(10))