import os

file = '/etc/passwd'
directory = '/etc'
link = '/bin/xzcat'

print(os.path.isfile(file))
print(os.path.isdir(directory))
print(os.path.islink(link))