'''FIND A SQUARE

You have coordinates of four points on a plane. Check whether they make a square.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following

(1,6), (6,7), (2,7), (9,1)
(4,1), (3,4), (0,5), (1,2)
(4,6), (5,5), (5,6), (4,5)
All numbers in input are integers between 0 and 10

OUTPUT SAMPLE:
Print results in the following way.

false
false
true
'''
import itertools
from math import sqrt
def f(test='(0,2), (1,2), (1,1), (1,0)\n'):
    test = test.rstrip().replace('),','').replace(')','').replace('(','').split()
    for i in range(len(test)):
        x = test[i].index(',')
        test[i] = [int(test[i][0:x]), int(test[i][x+1:])]
    d = {}
    for k in test:
        d[str(k[0])+'l'] = d.get(str(k[0])+'l',0) + 1
        d[str(k[1])+'r'] = d.get(str(k[1])+'r',0) + 1
        if d[str(k[1])+'r'] > 2 or d[str(k[0])+'l'] > 2:
            return "false"
    y = list(itertools.combinations(test, 2))
    z = []
    for i in y:
        if i[0] == i[1]:
            return "false"
        z.append(g(i[0][0], i[0][1], i[1][0], i[1][1]))
    count = 0
    mirror = 0
    for i in range(3):
        count = 0
        mirror = 0
        for j in range(i+1, 6):
            count+= z[i] == z[j]
            mirror+= (z[i][0] == z[j][0] and z[i][1] == -z[j][1])
            if count >= 1 and mirror >= 2:
                return "true"
    return "false"

def g(x1,y1, x2,y2):
    if (x2-x1) != 0:
        slope = ( (y2-y1) / (x2-x1) )
    else:
        slope = 0
    distance = sqrt( (x2-x1)**2 + (y2-y1)**2 )
    if abs(slope) < 1 and abs(slope) > 0:
        slope = 1 / slope
    return [ round(distance,4), (round(slope,4)) ]
