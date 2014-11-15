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

