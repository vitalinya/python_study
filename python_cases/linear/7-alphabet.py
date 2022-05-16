from string import ascii_lowercase
from random import randint

alphabet = ascii_lowercase
alphabet_num = len(alphabet)
letter_num = randint(0, alphabet_num - 1)
letter = alphabet[letter_num]
letter_index = letter_num + 1
print ('letter =', letter, 'index =', letter_index)