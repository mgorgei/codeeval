'''CALCULATE DISTANCE

You have coordinates of 2 points and need to find the distance between them.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following

(25, 4) (1, -6)
(47, 43) (-25,-11)

All numbers in input are integers between -100 and 100.

OUTPUT SAMPLE:
Print results in the following way.

26
90

You don't need to round the results you receive. They must be integer numbers.
'''
from math import sqrt
def f(test='(25, 4) (1, -6)'):
    p1, p2 = test.rstrip().split(") ")
    x1, y1 = p1.split(", ")
    x2, y2 = p2.split(", ")
    x1 = int(x1[1:])
    y1 = int(y1)
    x2 = int(x2[1:])
    y2 = int(y2[:-1])
    print(int(sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2)))
