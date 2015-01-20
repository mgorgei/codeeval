'''PREFIX EXPRESSIONS

You are given a prefix expression. Write a program which evaluates it.

INPUT SAMPLE:
Your program should accept a file as its first argument. The file contains one
prefix expression per line.
For example:

* + 2 3 4

Your program should read this file and insert it into any data structure you
like. Traverse this data structure and evaluate the prefix expression. Each
token is delimited by a whitespace. You may assume that sum ‘+’, multiplication
‘*’ and division ‘/’ are the only valid operators appearing in the test data.

OUTPUT SAMPLE:
Print to stdout the output of the prefix expression, one per line.
For example:

20

CONSTRAINTS:
The evaluation result will always be an integer ≥ 0.
The number of the test cases is ≤ 40.
'''
import operator
def f(test='* + 2 3 4\n'):#20... (2 + 3) * 4
    test = test.rstrip('\n').split()
    index = len(test) // 2
    summ = [int(test[index])]
    for j in range(index+1, len(test)):
        op = test[index-j+index]
        if op == '+':
            op = operator.add
        elif op == '*':
            op = operator.mul
        else:
            op = operator.truediv
        summ = list(map(op, summ, [int(test[j])] ))
    print(summ[0])
