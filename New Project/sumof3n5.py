# Hello World program in Python
    


def findSum():
    number = 0
    sumofnumbers = 0
    for number in xrange(0,1000):
        if(number % 3 == 0 or number % 5 == 0): 
            sumofnumbers += number
    return sumofnumbers
    
print findSum()    
