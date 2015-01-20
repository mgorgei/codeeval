'''MINIMUM PATH SUM

You are given an n*n matrix of integers. You can move only right and down.
Calculate the minimal path sum from the top left to the bottom right

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. The first
line will have the value of n(the size of the square matrix). This will be
followed by n rows of the matrix. (Integers in these rows will be comma
delimited). After the n rows, the pattern repeats. E.g.

2
4,6
2,8
3
1,2,3
4,5,6
7,8,9

OUTPUT SAMPLE:
Print out the minimum path sum for each matrix. E.g.

14
21
'''
def g(row, col, matrix, pathsum):
    pathsum+= matrix[row][col]
    if row == len(matrix)-1 and col == len(matrix[0])-1:
        return pathsum
    r,d = 0,0
    if row < len(matrix) - 1:
        r = g(row+1, col, matrix, pathsum)
    if col < len(matrix[0]) - 1:
        d = g(row, col+1, matrix, pathsum)
    return min(r,d) if r and d else max(r,d)

with open('t72.txt') as file:
    rows = 0
    matrix = []
    for test in file:
        test = test.rstrip('\n')
        if not rows:
            rows = int(test)
            matrix = []
            continue
        else:
            rows-=1
            matrix.append([int(x) for x in test.split(',')])
        if not rows:
            print(g(0,0, matrix, 0))

