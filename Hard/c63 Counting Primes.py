'''COUNTING PRIMES

Given two integers N and M, count the number of prime numbers between N and M
(both inclusive)

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains two comma separated positive integers. E.g.

2,10
20,30

OUTPUT SAMPLE:
Print out the number of primes between N and M (both inclusive)

4
2
'''
def isPrime(number):  
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
        count+= isPrime(i)
    return count
