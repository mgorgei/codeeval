'''SUDOKU

Sudoku is a number-based logic puzzle. It typically comprises of a 9*9 grid with
digits so that each column, each row and each of the nine 3*3 sub-grids that
compose the grid contains all the digits from 1 to 9. For this challenge, you
will be given an N*N grid populated with numbers from 1 through N and you have
to determine if it is a valid sudoku solution. You may assume that N will be
either 4 or 9. The grid can be divided into square regions of equal size, where
the size of a region is equal to the square root of a side of the entire grid.
Thus for a 9*9 grid there would be 9 regions of size 3*3 each.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains the value of N, a semicolon and the sqaure matrix of
integers in row major form, comma delimited. E.g.

4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2
4;2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1

OUTPUT SAMPLE:
Print out True/False if the grid is a valid sudoku layout. E.g.

True
False
'''
# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]
from math import sqrt
def create_grid(test='4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2'):
    test = test.rstrip().split(';')
    test[1] = test[1].split(',')
    grid = []
    for i in range(int(test[0])):
        slist = []
        for j in range(int(test[0])):
            slist.append(int(test[1][j + int(test[0])* i]))#0-15
        grid.append(slist)
    return grid

def check_sudoku(grid, n=9):
    try:
        rcount = 0
        for lst in grid:
            if len(lst) != n:
                raise
            rcount += 1
            for item in lst:
                if type(item) != int:
                    raise#return None
                if item < 0 or item > n:
                    raise#return None
        if rcount != n:
            return None
    except:
        print ("List is malformed or not a list of integers in range 0..{}".format(n))
        return None
    #check row validity
    for lst in grid:
        rdigits = [int(i) for i in range(1,n+1)]#[1,2,3,4,5,6,7,8,9]
        for digit in lst:
            if digit in rdigits:
                rdigits.remove(digit)
            elif digit == 0:
                pass
            else:
                return False#digit not found in row
    #check column validity
    for col in range(n):
        cdigits = [int(i) for i in range(1,n+1)]#[1,2,3,4,5,6,7,8,9]
        for i in range(n):
            if grid[i][col] in cdigits:
                cdigits.remove(grid[i][col])
            elif grid[i][col] == 0:
                pass
            else:
                return False#digit not found in row
    #check grid validity
    box = int(sqrt(n))
    for g in range(n):
        gdigits = [int(i) for i in range(1,n+1)]#[1,2,3,4,5,6,7,8,9]
        for i in range((g % box) * box, (g % box) * box + box):
            for j in range((g // box) * box, (g // box) * box + box):
                if grid[j][i] in gdigits:
                    gdigits.remove(grid[j][i])
                elif grid[j][i] == 0:
                    pass
                else:
                    return False#digit not found in row

    return True
