
def loopthrunumbers():
	n = 1
	ab = True
	sum = 0
	while ab :
		i = n
		sum = sum + i
		i = i - 1

		print str(n)+" - "+str(sum)
		ab = checkNumberofDivisors(sum)
		n = n + 1

def checkNumberofDivisors(number):
	i = 1
	c = 0
	if number % 2 != 0:
		return True

	while (i <= number/2):
		if number % i==0:
			c = c + 1
		i = i + 1
	print "count-" + str (c+1)
	if c + 1 >= 500:
		print "<<<<<<<<<"+ str(number)
		return False
	else:
		return True

loopthrunumbers()
	
	