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
'''You are given 3 coins of value 1, 3 and 5. You are also given a total which
you have to arrive at. Find the minimum number of coins to arrive at it.'''
