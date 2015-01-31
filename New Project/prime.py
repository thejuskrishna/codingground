def inputNumber(number):
    i = 2;
    for i in xrange(2, number/2):
        if number % i == 0 and number != i:
            number = number / i
            print(i)
        if number == i:
            return number
    return -1
print inputNumber(600851475143)
        