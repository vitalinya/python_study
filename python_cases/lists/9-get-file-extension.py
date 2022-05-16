from random import randint
from string import ascii_lowercase

extensions = ['txt','json','bin','exe','doc','yaml','xml','odt','mp3','mp4']
filename = ascii_lowercase[randint(0, len(extensions)-1)]
file = filename + '.' + extensions[randint(0, len(extensions)-1)]

file_split = file.split(".")

print(file)
print (file_split[-1])