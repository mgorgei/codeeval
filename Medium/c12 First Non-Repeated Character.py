'''FIRST NON-REPEATED CHARACTER

Write a program which finds the first non-repeated character in a string.

INPUT SAMPLE:
The first argument is a path to a file. The file contains strings.
For example:

yellow
tooth

OUTPUT SAMPLE:
Print to stdout the first non-repeated character, one per line.
For example:

y
h
'''
def f(test='yellow'):
    test = test.rstrip()
    for i in range(len(test)):
        if test.count(test[i]) == 1:
            print(test[i])
            break
