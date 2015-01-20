'''STACK IMPLEMENTATION

Write a program which implements a stack interface for integers. The interface
should have ‘push’ and ‘pop’ functions. Your task is to ‘push’ a series of
integers and then ‘pop’ and print every alternate integer.

INPUT SAMPLE:
Your program should accept a file as its first argument. The file contains a
series of space delimited integers, one per line.
For example:

1 2 3 4
10 -2 3 4

OUTPUT SAMPLE:
Print to stdout every alternate space delimited integer, one per line.
For example:

4 2
4 -2
'''
from collections import deque
def f(test='10 -2 3 4'):
    test = test.rstrip().split()
    stack = deque(test)
    result = ""
    for i in range( (len(stack)+ 1)//2 ):
        result+= stack.pop() + ' '
        stack.rotate(1)
    print(result[:-1])
