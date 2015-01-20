'''DECODE NUMBERS

You are given an encoded message containing only numbers. You are also provided
with the following mapping:

A : 1
B : 2
C : 3
...
Z : 26
Given an encoded message, count the number of ways it can be decoded.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file is a test-case and contains an encoded message of numbers. E.g.

12
123

You may assume that the test cases contain only numbers.

OUTPUT SAMPLE:
Print out the different number of ways it can be decoded. E.g.

2
3
NOTE: 12 could be decoded as AB(1 2) or L(12). Hence the number of ways to
decode 12 is 2.
'''
valid=['1','2','3','4','5','6','7','8','9','10','11','12','13','14',
       '15','16','17','18','19','20','21','22','23','24','25','26']
def f(test='1319'):#1 3 1 9,13 1 9, 13 19, 1 3 19; 4
    string = test.rstrip('\n')
    candidates = []
    g(string, '', candidates)
    print((candidates))

def g(original, out, candidates):
    if not original:
        candidates.append(out.lstrip(' '))
        return
    if original[:1] in valid:
        g(original[1:], out + ' ' + original[:1], candidates)
    if len(original) > 1 and original[:2] in valid:
        g(original[2:], out + ' ' + original[:2], candidates)

