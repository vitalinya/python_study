import os

def check_file(path,file):
	return file in os.listdir(path)

print(check_file('.','2.py'))
