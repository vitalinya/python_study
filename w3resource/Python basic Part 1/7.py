def extension(filename):
	ext = filename.split('.')
	return ext[-1]

print(extension('abc.java'))