'''SUM TO ZERO

You are given an array of integers. Count the numbers of ways in which the sum
of 4 elements in this array results in zero.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file consist of comma separated positive and negative integers. E.g.

2,3,1,0,-4,-1
0,-1,3,-2

OUTPUT SAMPLE:
Print out the count of the different number of ways that 4 elements sum to zero.
E.g.

2
1
'''
from itertools import combinations
def f(test='2,3,1,0,-4,-1\n'):
    test = [int(x) for x in test.rstrip().split(',')]
    test = list(combinations(test, 4))
    count = 0
    for item in test:
        res = ''
        for i in range(4):
            res+=str(item[i])+'+'
        if eval(res[:-1]) == 0:
            count+=1
    print(count)
