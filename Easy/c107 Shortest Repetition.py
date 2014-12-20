'''SHORTEST REPETITION

Write a program to determine the shortest repetition in a string. 
A string is said to have period p if it can be formed by concatenating one or
more repetitions of another string of length p. For example, the string
"xyzxyzxyzxyz" has period 3, since it is formed by 4 repetitions of the string
"xyz". It also has periods 6 (two repetitions of "xyzxyz") and 12 (one
repetition of "xyzxyzxyzxyz").

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
will contain a string of up to 80 non-blank characters. E.g.
abcabcabcabc
bcbcbcbcbcbcbcbcbcbcbcbcbcbc
dddddddddddddddddddd
adcdefg

OUTPUT SAMPLE:
Print out the smallest period of the input string. E.g.
3
2
1
7
'''
def f(test):
    for i in range(1,40):
        tempstr = test[0:i]
        for j in range(0,len(test), i):
            if tempstr != test[j:j+i]:
                break
        else:
            return i
    return i
