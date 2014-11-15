def f(test='''.........*
.*.*...*..
..........
..*.*....*
.*..*...*.
.........*
..........
.....*..*.
.*....*...
.....**...'''):
    test = test.rstrip('\n').split('\n')
    pool = []
    for line in test:
        pool.append(line)
    iterations = 10
    while iterations:
        new_pool = []
        for line in range(len(pool)):
            new_line = ""
            for cell in range(len(pool[line])):
                new_line+= '*' if life_death(cell,line,pool) else '.'
            new_pool.append(new_line)
        pool = new_pool
        iterations-= 1
    for line in pool:
        print(line)

def life_death(x, y, pool):
    alive = pool[y][x] == '*'
    nearby_cells = 0
    matrix = 1*(x > 0) + 2*(x + 1 < len(pool[0])) + 4*(y > 0) + 8*(y + 1 < len(pool))
    nearby_cells+= matrix & 9 == 9 and pool[y+1][x-1] == '*'
    nearby_cells+= matrix & 1 == 1 and pool[y][x-1] == '*'
    nearby_cells+= matrix & 5 == 5 and pool[y-1][x-1] == '*'
    nearby_cells+= matrix & 8 == 8 and pool[y+1][x] == '*'
    nearby_cells+= matrix & 4 == 4 and pool[y-1][x] == '*'
    nearby_cells+= matrix & 10 == 10 and pool[y+1][x+1] == '*'
    nearby_cells+= matrix & 2 == 2 and pool[y][x+1] == '*'
    nearby_cells+= matrix & 6 == 6 and pool[y-1][x+1] == '*'

    if alive:
        #Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        if nearby_cells < 2:
            return False
        #Any live cell with two or three live neighbors lives on to the next generation.
        if nearby_cells > 1 and nearby_cells < 4:
            return True
        #Any live cell with more than three live neighbors dies, as if by overcrowding.
        return False
    else:
        #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        return nearby_cells == 3
