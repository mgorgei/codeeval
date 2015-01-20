'''A PILE OF BRICKS

You have a pile of bricks. Every brick has it's index number and coordinates of
opposite vertices. 
You know that somewhere on the wall there is a rectangular hole, and you are
given coordinates of opposite vertices of that hole. 
Determine which bricks may pass through that hole. 
In situations where brick and hole have an equal sizes, we assume that it can
pass through this hole. 
All the holes are two-dimensional. All of the bricks are three-dimensional.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. The input
file contains several lines. Each line is one test case. 

Each line contains coordinates of opposite vertices of a hole (before the
vertical bar) separated by space bar and the list of bricks you need to check.
Each brick is enclosed in parentheses where the 1st number is a brick's index
number, the 2nd and 3rd group of numbers are brick's coordinates of opposite
vertices (separated by a space bar), each brick is divided by semicolon. E.g.

[4,3] [3,-3]|(1 [10,9,4] [9,4,2])
[-1,-5] [5,-2]|(1 [4,7,8] [2,9,0]);(2 [0,7,1] [5,9,8])
[-4,-5] [-5,-3]|(1 [4,8,6] [0,9,2]);(2 [8,-1,3] [0,5,4])

OUTPUT SAMPLE:
For each set of bricks produce a list of bricks (their index numbers in
ascending order separated by comma) that can pass through the hole. E.g.

1
1,2
-
'''
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
    result = ""
    for i in range(len(bricks)):
        bricks[i] = bricks[i].split()
        bricks[i][1] = [int(x) for x in bricks[i][1][1:-1].split(',') ]
        bricks[i][2] = [int(x) for x in bricks[i][2][1:-1].split(',') ]
        normal = [abs(bricks[i][1][0]-bricks[i][2][0]),
                  abs(bricks[i][1][1]-bricks[i][2][1]),
                  abs(bricks[i][1][2]-bricks[i][2][2])]
        normal = sorted(normal)
        if normal[0] <= hole[0] and normal[1] <= hole[1]:
            result += bricks[i][0] + ','
    if result:
        print(result[:-1])
    else:
        print('-')
