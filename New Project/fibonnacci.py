
def findFibSum(limit):
    a = 1
    b = 2
    num = 2
    sumfib = 2
    temp = 0
    while temp < limit:
        temp = a+b
        if temp % 2 == 0 :
            sumfib += temp
        a = b;
        b = temp;
        
    return sumfib
    
    
print findFibSum(4000000)
        
        
        