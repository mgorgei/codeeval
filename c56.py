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
