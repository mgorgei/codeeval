'''ROBOT MOVEMENTS

A robot is located at the top-left corner of a 4x4 grid. The robot can move
either up, down, left, or right, but can not visit the same spot twice. The
robot is trying to reach the bottom-right corner of the grid.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print out the unique number of ways the robot can reach its destination. (The
number should be printed as an integer whole number eg. if the answer is 10 (its
not !!), print out 10, not 10.0 or 10.00 etc)
'''
from copy import deepcopy
def f():
    traveled = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    print(int(g(0,0, traveled)))

def g(row, col, traveled):
    if row == 3 and col == 3:
        return 1
    elif traveled[row][col]:
        return 0
    traveled[row][col] = 1
    up, left, right, down = 0,0,0,0
    if row - 1 > -1:
        up = g(row-1, col, deepcopy(traveled))
    if col - 1 > -1:
        left = g(row, col-1, deepcopy(traveled))
    if col + 1 < len(traveled[0]):
        right = g(row, col+1, deepcopy(traveled))
    if row + 1 < len(traveled):
        down = g(row+1, col, deepcopy(traveled))
    return up + left + right + down
