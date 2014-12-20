'''N MOD M

Given two integers N and M, calculate N Mod M (without using any inbuilt modulus
operator).

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains two comma separated positive integers. E.g.
20,6
2,3
You may assume M will never be zero.

OUTPUT SAMPLE:
Print out the value of N Mod M
'''
def f(test):
    test = test.strip().split(',')
    a = int(test[0])
    b = int(test[1])
    if a < b:
        print(a)
    else:
        x = b
        while(1):
            if b == 1:
                print(0)
                break
            elif a == x:
                print(0)
                break
            elif x + b <= a:
                x = x + b
            else:
                print(a - x)
                break
