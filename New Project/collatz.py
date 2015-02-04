def collatz(number):
	c = 0
	while number > 1:
		#print number
		if number % 2 == 1:
			number = 3 * number + 1
		else:
			number = number / 2
		c = c + 1
	return c + 1

#print collatz(1000000)


def findNum(N):
	large = 1
	n = N
	temp = 1
	while n >= N/2:
		num = collatz(n)
		if num > large:
			print str(num) + "<<<" + str(n)
			temp = n
			large = num
		n = n - 1
	#print str(temp) + "<<<<" + str(large)	
	return temp

print findNum(1000000)
