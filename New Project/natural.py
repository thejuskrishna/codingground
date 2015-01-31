def sumofnatsq(low, upper):
	sum = 0
	while low <= upper:
		sum = sum + low
		low = low + 1
	return sum*sum

def sumofsqnatural(low, upper):
	sum = 0
	while low <= upper:
		sum = low*low + sum
		low = low + 1
	return sum

print sumofnatsq(1, 100) - sumofsqnatural(1, 100) 
