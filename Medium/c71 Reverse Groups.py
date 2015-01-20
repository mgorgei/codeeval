'''REVERSE GROUPS

Given a list of numbers and a positive integer k, reverse the elements of the
list, k items at a time. If the number of elements is not a multiple of k, then
the remaining items in the end should be left as is.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains a list of numbers and the number k, separated by a
semicolon. The list of numbers are comma delimited. E.g.

1,2,3,4,5;2
1,2,3,4,5;3

OUTPUT SAMPLE:
Print out the new comma separated list of numbers obtained after reversing. E.g.

2,1,4,3,5
3,2,1,4,5
'''
def f(test='1,2,3,4,5;2'):
    test = test.rstrip().split(';')
    sequence = test[0].split(',')
    length = int(test[1])
    result = ""
    for index in range(0, len(sequence), length):
        if index + length > len(sequence):
            result+= ','.join(sequence[index:]) + 'X'
            break
        for reverse in range(index + length - 1, index - 1, -1):
            result+= sequence[reverse] + ','
    print(result[:-1])
