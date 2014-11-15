'''
-tt tt t
-tt tt t
-tt tt t

-tt tt t
 || || |'''
from math import sqrt
def f(test='(0,1,3,4,6) (0,1,2,4)'):#5
    test = test.rstrip('\n').split(' ')
    test[0] = test[0][1:-1].split(',')#vertical
    test[1] = test[1][1:-1].split(',')#horizontal
    distance = sqrt(int(test[0][-1])**2 + int(test[1][-1])**2)
    slope = int(test[1][-1]) / int(test[0][-1])
    print(slope,distance)
