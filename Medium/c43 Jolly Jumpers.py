'''JOLLY JUMPERS

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla 

A sequence of n > 0 integers is called a jolly jumper if the absolute values of
the differences between successive elements take on all possible values 1
through n - 1. eg. 

1 4 2 3 

is a jolly jumper, because the absolute differences are 3, 2, and 1,
respectively. The definition implies that any sequence of a single integer is a
jolly jumper. Write a program to determine whether each of a number of sequences
is a jolly jumper. 

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain an integer n < 3000
followed by n integers representing the sequence. The integers are space
delimited.

OUTPUT SAMPLE:
For each line of input generate a line of output saying 'Jolly' or 'Not jolly'.
'''
def f(test='4 4 1 3 2'):
    test = [int(x) for x in test.rstrip().split()]
    jolly = [0]
    for i in range(1, len(test) -1):
        jolly.append(abs(test[i] - test[i+1]))
    if sorted(jolly) == list(range(len(test))):
        print('Jolly')
    else:
        print('Not jolly')
