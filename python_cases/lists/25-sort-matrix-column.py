from random import randint

M = 5
N = 5

matrix = [[randint(0,9) for x in range(M)] for y in range(N)]

for item in range(len(matrix)):
	print (matrix[item],end='\n')

print()
for count in range(0,M):
	for row in range(M-1):
		for col in range(N):
			if matrix[row][col] > matrix[row+1][col]:
				matrix[row+1][col],matrix[row][col] = matrix[row][col],matrix[row+1][col]
			else:
				continue

for item in range(len(matrix)):
	print (matrix[item],end='\n')
