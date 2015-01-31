import isPrime

def sumofprimes(number):
	i = 3
	sum = 2
	while(i < number):
		if isPrime.isPrimeNumber(i):
			sum = sum + i
			#print sum
		i = i + 2
	return sum

print sumofprimes(2000000)