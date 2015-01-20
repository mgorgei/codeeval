'''SUM OF INTEGERS

Write a program to determine the largest sum of contiguous integers in a list.

INPUT SAMPLE:
The first argument is a path to a filename containing a comma-separated list of
integers, one per line.
For example:

-10,2,3,-2,0,5,-15
2,3,-2,-1,10

OUTPUT SAMPLE:
Print to stdout the largest sum. In other words, of all the possible contiguous
subarrays for a given array, find the one with the largest sum, and print that
sum.
For example:

8
12
'''
def f(test='-10,2,3,-2,0,5,-15'):
    test = test.rstrip('\n').split(',')
    test = list(map(int, test))
    largest = -999
    for i in range(len(test)):
        for j in range(i, len(test)):
            summ = sum(test[i:j+1])
            if summ > largest:
                largest = summ
    print(largest)
