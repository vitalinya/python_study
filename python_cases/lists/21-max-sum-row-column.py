from random import randint

M = 5
N = 5

matrix = [[randint(0,5) for x in range(M)] for y in range(N)]

for item in range(len(matrix)):
	print (matrix[item],end='\n')

row_sum = [0]*M
col_sum = [0]*N
for row in range(M):
	for col in range(N):
		row_sum[row] += matrix[row][col]
		col_sum[col] += matrix[row][col]

print(max(row_sum),row_sum.index(max(row_sum)))
print(max(col_sum),col_sum.index(max(col_sum)))