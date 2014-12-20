'''ODD NUMBERS

Print the odd numbers from 1 to 99.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print the odd numbers from 1 to 99, one number per line. 
'''
def f(n=99):
    print('\n'.join([str(i) for i in range(1, n+1, 2)]))
