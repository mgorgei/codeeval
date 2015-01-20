'''WORD SEARCH

Given a 2D board and a word, find if the word exists in the grid. The word can
be constructed from letters of sequentially adjacent cell, where adjacent cells
are those horizontally or vertically neighboring. The same letter cell may not
be used more than once.

INPUT SAMPLE:

The board to be used may be hard coded as:

[
[ABCE],
[SFCS],
[ADEE]
]

Your program should accept as its first argument a path to a filename. Each line
in this file contains a word. E.g.

ASADB
ABCCED
ABCF

OUTPUT SAMPLE:
Print out True if the word exists in the board, False otherwise. E.g.

False
True
False
'''
import copy
board = ['ABCE','SFCS','ADEE']
def f(test='ABCCED'):
    global board
    traveled = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    indices = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == test[0]:
                indices.append( (i,j) )
    test = test.rstrip('\n')
    for index in indices:
        if g(index[0], index[1], test, copy.deepcopy(traveled)) == True:
            print(True)
            break
        #traveled = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    else:
        print (False)

def g(x, y, test, traveled):#, chain=''):
    if test == '':
        return True
    elif traveled[x][y]:
        return False
    elif board[x][y] != test[0]:
        return False
    traveled[x][y] = 1
    up, left, right, down = False,False,False,False
    if x - 1 > -1:
        up = g(x-1, y, test[1:], copy.deepcopy(traveled))#, chain + board[x][y])
    if y - 1 > -1:
        left = g(x, y-1, test[1:], copy.deepcopy(traveled))#, chain + board[x][y])
    if y + 1 < len(board[0]):
        right = g(x, y+1, test[1:], copy.deepcopy(traveled))#, chain + board[x][y])
    if x + 1 < len(board):
        down = g(x+1, y, test[1:], copy.deepcopy(traveled))#, chain + board[x][y])
    return up or left or right or down#magic
    
    
