import math

def isPrimeNumber(number):
	if number == 2:
		return True

	if number % 2 == 0:
		return False
	i = 3
	while i<= math.sqrt(number):
		if number % i == 0:
			return False
		i = i + 2

	return True

