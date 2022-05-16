from random import randint

M = 5
N = 5

matrix = [[randint(0,5) for x in range(M)] for y in range(N)]

for item in range(len(matrix)):
	print (matrix[item],end='\n')

print()

main_diag = 0
slave_diag = 0

for row in range(M):
	for col in range(N):
		if col == row:
			main_diag += matrix[row][col]
			slave_diag += matrix[row][-col-1]

