def f(test='[-4,-5] [-5,-3]|(1 [4,8,6] [0,9,2]);(2 [8,-1,3] [0,5,4])'):
    test = test.rstrip().split('|')
    test[0] = test[0].split()
    test[0][0] = test[0][0][1:-1].split(',')
    test[0][1] = test[0][1][1:-1].split(',')
    hole = [abs( int(test[0][0][0]) - int(test[0][1][0]) ),
            abs( int(test[0][0][1]) - int(test[0][1][1]) )]
    hole = sorted(hole)
    bricks = test[1]
    bricks = bricks.replace('(','').replace(')','').split(';')
    result = []
    for i in range(len(bricks)):
        bricks[i] = bricks[i].split()
        bricks[i][1] = [int(x) for x in bricks[i][1][1:-1].split(',') ]
        bricks[i][2] = [int(x) for x in bricks[i][2][1:-1].split(',') ]
        normal = [abs(bricks[i][1][0]-bricks[i][2][0]),
                  abs(bricks[i][1][1]-bricks[i][2][1]),
                  abs(bricks[i][1][2]-bricks[i][2][2])]
        normal = sorted(normal)
        if normal[0] <= hole[0] and normal[1] <= hole[1]:
            result.append(int(bricks[i][0]))
    if result:
        result = sorted(result)
        result = [str(s) for s in result]
        print(','.join((result)))
    else:
        print('-')
