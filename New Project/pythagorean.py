import math

def pyth(a, b, c):
	for i in xrange(c, 999):
		for j in xrange(b, 666):
			for k in xrange(a, 333):
				if(i + j + k == 1000):
					if i == math.sqrt(k*k + j*j):
						print i*j*k	
						print i
						print j
						print k
						return

pyth(1, 1, 1)