import math

def isPalindrome(number):
    rev = 0
    digit = 0
    n = number
    i = 0
    while number != 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number/10
        i = i+1
    if rev == n:
        return True
        
    return False


def check():
    a = 999
    b = 999
    temp = 0
    while a >= 499:
        b = 999
        while b>=100:
            if isPalindrome(a*b):
                print "found"
                print a
                print b
                if a*b > temp:
                    temp = a*b
                
            else:
                print "no-" + str(a) + " x " + str(b) + " = " + str(a*b)
            b = b - 1
        a = a - 1
    return temp
    
print check()
        