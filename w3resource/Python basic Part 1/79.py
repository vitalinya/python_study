from random import randint
import sys

x = [randint(0, 9) for x in range(10)]

print(sys.getsizeof(x))
