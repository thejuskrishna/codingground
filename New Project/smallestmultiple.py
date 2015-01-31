import isPrime

def primemultiples(number):
	i = 1
	n = number
	while number >= 2:
		if isPrime.isPrimeNumber(number):
			temp = isPowered(number, n)
			i = i * temp
			#print i
		number = number - 1
	return i

def isPowered(number, n):
	if number == n: 
		return number
	temp = number 	

	while number < n: 
		number = number * temp 
	return number/temp

print primemultiples(20)


