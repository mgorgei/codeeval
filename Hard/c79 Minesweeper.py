'''MINESWEEPER

You will be given an M*N matrix. Each item in this matrix is either a '*' or a
'.'. A '*' indicates a mine whereas a '.' does not. The objective of the
challenge is to output a M*N matrix where each element contains a number (except
the positions which actually contain a mine which will remain as '*') which
indicates the number of mines adjacent to it. Notice that each position has at
most 8 adjacent positions e.g. left, top left, top, top right, right, ...

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains M,N, a semicolon and the M*N matrix in row major form. E.g.

3,5;**.........*...
4,4;*........*......

OUTPUT SAMPLE:
Print out the new M*N matrix (in row major form) with each position(except the
ones with the mines) indicating how many adjacent mines are there. E.g.

**100332001*100
*10022101*101110
'''
#bitwise
def f(test='3,5;***..*.*..***..'):#**.........*...;**100332001*100
    test = test.rstrip('\n').split(';')
    test[0] = test[0].split(',')
    row = int(test[0][0])
    col = int(test[0][1])
    minefield = []
    for i in range(row):
        slist = []
        for j in range(col):
            slist.append(test[1][i * col + j])
        minefield.append(slist)
    for y in range(row):
        for x in range(col):
            if minefield[y][x] == '.':
                minefield[y][x] = str(count(x,y,minefield))
    result = ''
    for line in minefield:
        result+= ''.join(line)
    print(result)

def count(x, y, minefield):
    mines = 0
    matrix = 1*(x > 0) + 2*(x + 1 < len(minefield[0])) + 4*(y > 0) + 8*(y + 1 < len(minefield))
    mines+= matrix & 9 == 9 and minefield[y+1][x-1] == '*'
    mines+= matrix & 1 == 1 and minefield[y][x-1] == '*'
    mines+= matrix & 5 == 5 and minefield[y-1][x-1] == '*'
    mines+= matrix & 8 == 8 and minefield[y+1][x] == '*'
    mines+= matrix & 4 == 4 and minefield[y-1][x] == '*'
    mines+= matrix & 10 == 10 and minefield[y+1][x+1] == '*'
    mines+= matrix & 2 == 2 and minefield[y][x+1] == '*'
    mines+= matrix & 6 == 6 and minefield[y-1][x+1] == '*'
    return mines
