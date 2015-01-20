'''MINIMUM COINS

You are given 3 coins of value 1, 3 and 5. You are also given a total which you
have to arrive at. Find the minimum number of coins to arrive at it.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains a positive integer number which represents the total you
have to arrive at. E.g.

11
20

OUTPUT SAMPLE:
Print out the minimum number of coins required to arrive at the total. E.g.

3
4
'''
def f(s):
    s = int(s)
    count = 0
    while s:
        if s > 4:
            s-=5
        elif s >2:
            s-=3
        else:
            s-=1
        count+=1
    return count
