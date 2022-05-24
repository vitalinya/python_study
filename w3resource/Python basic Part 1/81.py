from random import randint
import string
abc = string.ascii_lowercase
strings = [abc[randint(0, len(abc)-1)] for x in range(10)]

print(strings)
print(' '.join(strings))