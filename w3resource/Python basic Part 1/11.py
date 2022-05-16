def docs(function):
	return help(function.strip('()'))

docs('abs()')