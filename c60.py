'''
how far can monkey reach on the 0 axis? to determine size of graph
sum digits of x and y  <=  19
99=>18
199=>19
299=>20
298=>19
travel in four directions recursively
increment count if position is untraveled
'''
#traveled = [[0]*298]*298
def g(x, y):
    global traveled
g(0, 0)
