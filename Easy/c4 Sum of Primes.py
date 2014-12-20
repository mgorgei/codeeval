'''Sum of Primes

Write a program which determines the sum of the first 1000 prime numbers.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print to stdout the sum of the first 1000 prime numbers.

3682913
'''
def f(n=1000):
    count = 1
    sum_primes = 0
    num = 3
    while (count < n):
        if isPrime(num):
            sum_primes+= num
            count+=1
        num+=2#skip even numbers since they are clearly not prime
    print(sum_primes + 2)#2 is prime, but does not align with the optimization

def isPrime(number):  
    if number <= 1:
        return False
    for check in range(2, number):
        if (number % check) == 0:
            return False
    return True
