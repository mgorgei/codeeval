'''STRING LIST

Credits: Challenge contributed by Max Demian. 

You are given a number N and a string S. Print all of the possible ways to write
a string of length N from the characters in string S, comma delimited in
alphabetical order.

INPUT SAMPLE:
The first argument will be the path to the input filename containing the test
data. Each line in this file is a separate test case. Each line is in the
format: N,S i.e. a positive integer, followed by a string (comma separated). E.g.

1,aa
2,ab
3,pop

OUTPUT SAMPLE:
Print all of the possible ways to write a string of length N from the characters
in string S comma delimited in alphabetical order, with no duplicates. E.g.

a
aa,ab,ba,bb
ooo,oop,opo,opp,poo,pop,ppo,ppp
'''
import itertools
def f(test):
    test = test.rstrip().split(',')
    test[1] = set(test[1])
    result = ''
    x = itertools.product(test[1], repeat=int(test[0]))
    x = sorted(x)
    for i in x:
        result+= ''.join(i) + ','
    print(result[:-1])
