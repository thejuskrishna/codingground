import isPrime

def nthprime(number):
	i = 2
	c = 0
	while (c < number):
		if isPrime.isPrimeNumber(i):
			c = c + 1
		i = i + 1
	return i - 1

print nthprime(10001)