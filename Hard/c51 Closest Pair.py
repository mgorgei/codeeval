'''CLOSEST PAIR

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla 

You will be given the x/y co-ordinates of several locations. You will be laying
out 1 cable between two of these locations. In order to minimise the cost, your
task is to find the shortest distance between a pair of locations, so that pair
can be chosen for the cable installation.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. The input
file contains several sets of input. Each set of input starts with an integer N
(0<=N<=10000), which denotes the number of points in this set. The next N line
contains the coordinates of N two-dimensional points. The first of the two
numbers denotes the X-coordinate and the latter denotes the Y-coordinate. The
input is terminated by a set whose N=0. This set should not be processed. The
value of the coordinates will be less than 40000 and non-negative. eg.

5
0 2
6 67
43 71
39 107
189 140
0

OUTPUT SAMPLE:
For each set of input produce a single line of output containing a floating
point number (with four digits after the decimal point) which denotes the
distance between the closest two points. If there is no such two points in the
input whose distance is less than 10000, print the line INFINITY. eg.

36.2215
'''
from math import sqrt
def f():
    with open('t51a.txt') as file:
        points = []
        for test in file:
            if test.find(' ') != -1:
                test = test.rstrip('\n').split(' ')
                points.append((int(test[0]), int(test[1])))
            else:
                if len(points) == 0:
                    continue
                lowest = 10000.0000
                for i in range(len(points) - 1):
                    for j in range(i+1, len(points)):
                        temp = sqrt( (points[i][0] - points[j][0])**2 +
                                     (points[i][1] - points[j][1])**2 )
                        if temp < lowest:
                            lowest = temp
                if lowest == 10000.0000:
                    print(INFINITY)
                else:
                    print("{:.4f}".format(lowest))
                points.clear()
