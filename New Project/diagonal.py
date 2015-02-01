
def readFileAndReturnMatrix(file):
	f = open(file, 'r')
	mat = [[0 for x in range(20)] for x in range(20)]
	i = 0
	for line in f:
		mat[i] = line.split(' ')
		i = i + 1
	return mat
def check(temp, large):
	print temp
	if temp > large:
		return temp
	else:
		return large

def print4(a, b, c, d):
	print str(a) + "." + str(b) + "." + str(c) + "." + str(d)
	e = a*b*c*d
	print e
	return e

def find4():
	mat = readFileAndReturnMatrix('diagonal.txt')
	i = 0
	prod = 1
	temp = 1
	#print len(mat)
	while i < len(mat):
		j = 0
		#print len(mat[i])
		while j < len(mat[i]):
			if i - 3 >= 0:
				temp = print4(int(mat[i][j]), int(mat[i-1][j]), int(mat[i-2][j]), int(mat[i-3][j]))
			prod = check(temp, prod)
			if j - 3 >= 0:
				temp = print4(int(mat[i][j]), int(mat[i][j-1]), int(mat[i][j-2]), int(mat[i][j-3]))
			prod = check(temp, prod)
			if i + 3 <= len(mat) - 1:
				temp = print4(int(mat[i][j]), int(mat[i+1][j]), int(mat[i+2][j]), int(mat[i+3][j]))
			prod = check(temp, prod)
			if j + 3 <= len(mat[i]) - 1:
				temp = print4(int(mat[i][j]), int(mat[i][j+1]), int(mat[i][j+2]), int(mat[i][j+3]))
			prod = check(temp, prod)
			if j + 3 <= len(mat[i]) - 1 and i + 3 <= len(mat) - 1:
				temp = print4(int(mat[i][j]), int(mat[i + 1][j + 1]), int(mat[i + 2][j + 2]), int(mat[i + 3][j + 3]))  
			prod = check(temp, prod)
			if j - 3 >= 0 and i - 3 >= 0:
				temp = print4(int(mat[i][j]), int(mat[i - 1][j - 1]), int(mat[i - 2][j - 2]), int(mat[i - 3][j - 3]))  
			prod = check(temp, prod)
			if j - 3 >= 0 and i + 3 <= len(mat) - 1:
				temp = print4(int(mat[i][j]), int(mat[i + 1][j - 1]), int(mat[i + 2][j - 2]), int(mat[i + 3][j - 3]))  
			prod = check(temp, prod)
			j = j + 1
		i = i + 1
	return prod	

print find4()