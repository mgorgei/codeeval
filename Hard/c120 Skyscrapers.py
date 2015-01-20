'''SKYSCRAPERS

You are to design a program which helps you in drawing the skyline of a city.
You are given the locations of the buildings represented by triples (L, H, R)
where L and R are left and right coordinates of the building and H is the height
of the building. All buildings are rectangular in shape and they are standing on
a very flat surface. E.g. 
 
 
On the first diagram the buildings are represented by the following triples:

(1,2,3); (2,4,6); (4,5,5); (7,3,11); (9,2,14); (13,7,15); (14,3,17)
The drawing line as shown on the second diagram is described by the following
sequence:

1 2 2 4 4 5 5 4 6 0 7 3 11 2 13 7 15 3 17 0

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain the list of triples
semicolon separated. E.g.

(1,2,3);(2,4,6);(4,5,5);(7,3,11);(9,2,14);(13,7,15);(14,3,17)
(2,22,3);(6,12,10);(15,6,21)
(1,2,6);(9,23,22);(22,6,24);(8,14,19);(23,12,30)

OUTPUT SAMPLE:
The output must describe the drawing line as a vector
(X1,H1,X2,H2,X3,H3,X3,Xn-1,Hn-1,Xn) where X is a x-coordinate of a point where
the line is changing its direction from horizontal to vertical, and H is a
height of the vertical line. You're drawing continuously by starting at the
bottom of the first left building and finishing at the bottom of the right
building. So for each test case print out the drawing line in a way as it is
shown below.

1 2 2 4 4 5 5 4 6 0 7 3 11 2 13 7 15 3 17 0
2 22 3 0 6 12 10 0 15 6 21 0
1 2 6 0 8 14 9 23 22 6 23 12 30 0
'''
from collections import deque
def f(test='(1,2,3);(2,4,6);(4,5,5);(7,3,11);(9,2,14);(13,7,15);(14,3,17)'):#1 2 2 4 4 5 5 4 6 0 7 3 11 2 13 7 15 3 17 0
    sky = [( int(l),int(h),int(r) ) for l,h,r in (t.strip()[1:-1].split(',') for t in test.rstrip('\n').split(';'))]
    left = sorted([(l,h) for l,h,r in sky], key=lambda x:x[0])
    right = sorted([(r,h) for l,h,r in sky], key=lambda x:x[0])
    sky = sorted(sky, key=lambda x:x[0])
    height = 0
    result = []
    lastx = -1
    for x in range(sky[0][0], right[-1][0] + 1):#10001):
        elevator = []
        for b in sky:
            if b[0] > x:
                break#really naive computational savings
            if x >= b[0] and x < b[2]:
                elevator.append(b[1])
        if elevator:
            if lastx != -1 and height == 0:
                result.append(str(lastx))
                result.append(str(0))
            if height != max(elevator):
                height = max(elevator)
                result.append(str(x))
                result.append(str(height))
        else:
            if height != 0:
                lastx = x
                height = 0
    else:
        result.append(str(lastx))
        result.append(str(0))
    print(' '.join(result))
'''f('(1,2,3);(2,4,6);(4,5,5);(7,3,11);(9,2,14);(13,7,15);(14,3,17)')
f('(2,22,3);(6,12,10);(15,6,21)')
f('(1,2,6);(9,23,22);(22,6,24);(8,14,19);(23,12,30)')

1 2 2 4 4 5 5 4 6 0 7 3 11 2 13 7 15 3 17 0
2 22 3 0 6 12 10 0 15 6 21 0
1 2 6 0 8 14 9 23 22 6 23 12 30 0
'''
