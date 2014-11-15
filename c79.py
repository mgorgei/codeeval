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
