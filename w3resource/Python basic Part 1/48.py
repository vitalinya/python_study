string = '2626'

def convert(string):
	if '.' in string:
		return float(string)
	else:
		return int(string)

print(type(convert(string)))