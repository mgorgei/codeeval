def isPrime2(number):  
    if number <= 1:
        return False
    for check in range(2, number):
        if (number%check) == 0:
            return False
    return True

def f(test='2,10\n'):
    test = test.rstrip().split(',')
    count = 0
    for i in range(int(test[0]), int(test[1]) + 1):
        count+= isPrime2(i)
    return count
