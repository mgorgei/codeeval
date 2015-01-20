'''STRING ROTATION

You are given two strings. Determine if the second string is a rotation of the
first string.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains two comma separated strings. E.g.

Hello,lloHe
Basefont,tBasefon

OUTPUT SAMPLE:
Print out True/False if the second string is a rotation of the first. E.g.

True
True
'''
def f(test='Hello,lloHe'):
    test = test.rstrip().split(',')
    if len(test[0]) != len(test[1]):
        return False
    for i in range(len(test[0])):
        if test[0] == (test[1][i:] + test[1][:i]):
            return True
    return False
