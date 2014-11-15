#brute
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
