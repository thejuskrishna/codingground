def isInt(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def readFileAndReturnSum(file):
	f = open(file, 'r')
	mat = [[0 for x in range(20)] for x in range(20)]
	i = 0
	sum = 0
	for line in f:
		sum = sum + int(line)
	stringofnumber = str(sum)
	string2 = ""
	while i < 10:
		string2 = string2 + stringofnumber[i]
		i = i + 1
	#print string2
	return int(string2)

print readFileAndReturnSum('input.txt')

