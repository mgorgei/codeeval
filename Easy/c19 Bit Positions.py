'''BIT POSITIONS

Given a number n and two integers p1,p2 determine if the bits in position p1 and
p2 are the same or not. Positions p1 and p2 are 1 based.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated
list of 3 integers, one list per line. E.g.

86,2,3
125,1,2

OUTPUT SAMPLE:

Print to stdout, 'true'(lowercase) if the bits are the same,
else 'false'(lowercase). E.g.

true
false
'''
def f(test='86,2,3'):
    n, p1, p2 = list(map(int, test.rstrip().split(',')))
    n_as_binary = bin(n)
    print(str(n_as_binary[-p1] == n_as_binary[-p2]).lower())
