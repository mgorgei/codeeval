'''LONGEST COMMON SUBSEQUENCE

You are given two sequences. Write a program to determine the longest common
subsequence between the two strings (each string can have a maximum length of 50
characters). NOTE: This subsequence need not be contiguous. The input file may
contain empty lines, these need to be ignored.

INPUT SAMPLE:
The first argument will be a path to a filename that contains two strings per
line, semicolon delimited. You can assume that there is only one unique
subsequence per test case. E.g.

XMJYAUZ;MZJAWXU

OUTPUT SAMPLE:
The longest common subsequence. Ensure that there are no trailing empty spaces
on each line you print. E.g.

MJAU
'''
def LCS_length(X,Y):
    m = len(X) + 1
    n = len(Y) + 1
    b = [[0 for i in range(0, n)] for j in range(0, m)]
    c = [[0 for i in range(0, n)] for j in range(0, m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "Y"
            elif c[i-1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "U"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "L"
    return (c,b)

def print_LCS(b, X, i, j):
    global result
    if i == 0 or j == 0:
        return
    if b[i][j] == "Y":
        print_LCS(b, X, i-1, j-1)
        result+=X[i-1]
    elif b[i][j] == "U":
        print_LCS(b, X, i-1, j)
    else:
        print_LCS(b, X, i, j-1)

result = ""
def f(test='XMJYAUZ;MZJAWXU\n'):
    global result
    result = ""
    X,Y = test.rstrip('\n').split(';')
    c,b = LCS_length(X,Y)
    print_LCS(b, X, len(b)-1, len(b[0])-1)
    print(result)
