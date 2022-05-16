from random import randint

M = 5
N = 5

matrix = [[randint(0,5) for x in range(M)] for y in range(N)]

for item in range(len(matrix)):
	print (matrix[item],end='\n')

print()

for row in range(M):
	for col in range(N):
		if col == row:
			matrix[row][col],matrix[row][-col-1] = matrix[row][-col-1],matrix[row][col]

for item in range(len(matrix)):
	print (matrix[item],end='\n')

