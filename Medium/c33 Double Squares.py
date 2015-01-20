'''DOUBLE SQUARES

Credits: This challenge appeared in the Facebook Hacker Cup 2011.
A double-square number is an integer X which can be expressed as the sum of two
perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. Your
task in this problem is, given X, determine the number of ways in which it can
be written as the sum of two squares.

For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as
being different). On the other hand, 25 can be written as 5^2 + 0^2 or as 4^2 + 3^2. 
NOTE: Do NOT attempt a brute force approach. It will not work. The following
constraints hold: 
0 <= X <= 2147483647 
1 <= N <= 100

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. You
should first read an integer N, the number of test cases. The next N lines will
contain N values of X.

5
10
25
3
0
1

OUTPUT SAMPLE:
E.g.

1
2
0
1
1
'''
from math import sqrt
def f(test='10'):
    n = int(test)
    count = 0
    stop = int(sqrt(n / 2.0)) + 1 
    for i in range(stop):
        if sqrt(n-i*i).is_integer():
            count+=1
    return count

'''print (f(20) == 1,f(25) == 2,f(17) == 1,f(13) == 1,
       f(10) == 1,f(8) == 1,f(5) == 1,f(2) == 1,
       f(1) == 1,f(0) == 1,f(48612265) == 32, f(50) == 2)'''
