'''PASS TRIANGLE

By starting at the top of the triangle and moving to adjacent numbers on the row
below, the maximum total from top to bottom is 27.

   5
  9 6
 4 6 8
0 7 1 5
5 + 9 + 6 + 7 = 27

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following:

   5
  9 6
 4 6 8
0 7 1 5

You make also check full input file which will be used for your code evaluation.

OUTPUT SAMPLE:
The correct output is the maximum sum for the triangle. So for the given example
the correct answer would be

7
'''
def f(s='triangle.txt'):
    test_cases = open(s)
    result = 0
    lastpos = 0
    master = []
    for test in test_cases:
        test = [int(x) for x in test.split()]
        master.append(test)
    #have now converted file into list of lists of ints
    for i in range(len(master) - 2, -1, -1):
        for j in range(len(master[i])):
            master[i][j]+= max(master[i+1][j],master[i+1][j+1])
    return master[0][0]
