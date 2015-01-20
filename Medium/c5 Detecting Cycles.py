'''DETECTING CYCLES

Given a sequence, write a program to detect cycles within it.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename containing
a sequence of numbers (space delimited). The file can have multiple such lines.
E.g

2 0 6 3 1 6 3 1 6 3 1
3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49
1 2 3 1 2 3 1 2 3

OUTPUT SAMPLE:
Print to stdout the first cycle you find in each sequence. Ensure that there are
no trailing empty spaces on each line you print. E.g.

6 3 1
49
1 2 3
'''
def f(test='2 0 6 3 1 6 3 1 6 3 1'):#6 3 1
    test = test.rstrip('\n').split()
    for index, value in enumerate(test):
        if test.count(value) > 1:
            return ' '.join(test[index: test.index(value, index+1)])
