# How much does it cost to get from (i1, j) to (i2, j) by going up
# or down only?
def sum_to(i1, i2, j, matrix):
	x1 = min(i1, i2)
	x2 = max(i1, i2)
	return sum([matrix[x][j] for x in range(x1, x2+1)])
 
# Returns the minimum path sum that goes from any entry in the
# leftmost column to entry (i, j).
def compute_min_path_entry(i, j, matrix, min_path):
	n = len(matrix)
	# Possible paths: take the minimum cost path to somewhere in the
	# (j-1)th column, go right, and then go up or down until reaching
	# (i, j).
	possibilities = [min_path[x][j-1] + sum_to(x, i, j, matrix)
	for x in range(n)]
	return min(possibilities)
 
f = open("matrix.txt", "r")
contents = f.read()
f.close()
 
matrix = [[int(x) for x in line.split(",")]
			for line in contents.split("\n")[:-1]]
n = len(matrix) # assumes matrix is square
 
# Initialize min_path.
# min_path[x,y] will hold the minimal path sum starting at any entry in the
# leftmost column and ending at (x,y).
min_path = [[-1 for y in row] for row in matrix]
for i in range(n):
	min_path[i][0] = matrix[i][0]
 
# When min_path has been filled up to the j'th column, we can fill in
# the (j+1)st column.
for j in range(1, n):
	for i in range(n):
		min_path[i][j] = compute_min_path_entry(i, j, matrix, min_path)
 
result = min([min_path[i][n-1] for i in range(n)])
print result