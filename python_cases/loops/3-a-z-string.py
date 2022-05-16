from random import randint

ascii_start = randint(97,122)
ascii_end = randint(97,122)

if ascii_start > ascii_end:

	ascii_start,ascii_end = ascii_end,ascii_start

letter_start = chr(ascii_start)
letter_end = chr(ascii_end)

print('%s-%s' % (letter_start,letter_end))

for i in range(ord(letter_start),ord(letter_end)+1):
	print(chr(i), end=' ')	