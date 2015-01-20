'''NUMBER PAIRS

You are given a sorted array of positive integers and a number 'X'. Print out
all pairs of numbers whose sum is equal to X. Print out only unique pairs and
the pairs should be in ascending order

INPUT SAMPLE:
Your program should accept as its first argument a filename. This file will
contain a comma separated list of sorted numbers and then the sum 'X', separated
by semicolon. Ignore all empty lines. If no pair exists, print the string NULL
e.g.

1,2,3,4,6;5
2,4,5,6,9,11,15;20
1,2,3,4;50

OUTPUT SAMPLE:
Print out the pairs of numbers that equal to the sum X. The pairs should
themselves be printed in sorted order i.e the first number of each pair should
be in ascending order. E.g.

1,4;2,3
5,15;9,11
NULL
'''
from itertools import combinations
def f(test='2,4,5,6,9,11,15;20'):
    test = test.rstrip().split(';')
    test[0] = [int(x) for x in test[0].split(',')]
    test[1] = int(test[1])
    combo = combinations(test[0],2)
    result = ""
    for pair in combo:
        if pair[0] + pair[1] == test[1]:
            result+= str(pair[0]) + ',' + str(pair[1]) + ';'
    if result == "":
        print(NULL)
    else:
        print(result[:-1])
