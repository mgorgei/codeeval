'''POINT IN CIRCLE

Having coordinates of the center of a circle, it's radius and coordinates of a
point you need to define whether this point is located inside of this circle.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following

Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)
Center: (5.05, -11); Radius: 21.2; Point: (-31, -45)
Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)
All numbers in input are between -100 and 100

OUTPUT SAMPLE:
Print results in the following way.

true
false
true
'''
def f (test='Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)'):
    test = test.strip().split(';')
    center = test[0][test[0].index('(') + 1:-1]
    center = [float(x) for x in center.split(',')]
    radius = test[1][test[1].index(':') + 1:]
    radius = float(radius)
    point =  test[2][test[2].index('(') + 1:-1]
    point =  [float(x) for x in point.split(',')]
    return (point[0] - center[0])**2 + (point[1] - center[1])**2 <= radius**2
