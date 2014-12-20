'''SUM OF DIGITS

Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:
The first argument will be a path to a filename containing positive integers,
one per line. E.g.

23
496

OUTPUT SAMPLE:
Print to stdout, the sum of the numbers that make up the integer,
one per line. E.g.

5
19
'''
def f(test='23'):
    test = test.rstrip()
    print(sum([int(char) for char in test]))
