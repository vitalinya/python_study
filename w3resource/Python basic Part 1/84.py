from random import randint

string = 'abbcccddddeeeee'

letter = string[randint(0, len(string)-1)]

print (letter)
print (string.count(letter))