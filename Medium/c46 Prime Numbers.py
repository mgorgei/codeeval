'''PRIME NUMBERS

Print out the prime numbers less than a given number N. For bonus points your
solution should run in N*(log(N)) time or better. You may assume that N is
always a positive integer.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain an integer
n < 4,294,967,295. E.g.

10
20
100

OUTPUT SAMPLE:

For each line of input, print out the prime numbers less than N, in ascending
order, comma delimited. (There should not be any spaces between the comma and
numbers) E.g.

2,3,5,7
2,3,5,7,11,13,17,19
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
'''
def f(test='10'):
    n = int(test.strip())
    nlist = []
    for i in range(0, n+1):
        nlist.append([i, True])
    start = 2
    while start < n:
        for j in range(start, n+1, start):
            if j != start:
                nlist[j][1] = False
        for j in range(start+1, n+1):
            if nlist[j][1] == True:
                start = j
                break
        else:
            break
    result = ""
    for i in range(2, n):
        if nlist[i][1]:
            result+=str(nlist[i][0]) + ','
    print(result[:-1])
