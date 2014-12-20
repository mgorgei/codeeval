'''FIBONACCI SERIES

The Fibonacci series is defined as:
F(0) = 0; F(1) = 1;F(n) = F(n–1) + F(n–2) when n>1.
Given an integer n≥0, print out the F(n).

INPUT SAMPLE:
The first argument will be a path to a filename containing integer numbers, one
per line. E.g.

5
12

OUTPUT SAMPLE:
Print to stdout, the fibonacci number, F(n). E.g.

5
144
'''
def f(test='5'):
    print(fibonacci(int(test.rstrip())))    

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
