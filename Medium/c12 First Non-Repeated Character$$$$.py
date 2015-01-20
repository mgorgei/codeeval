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
    '''test = test.rstrip()
    uniq = []
    count = []
    for char in test:
        if not char in uniq:
            uniq.append(char)
            count.append(1)
        else:
            count[uniq.index(char)]+= 1
    index = 0
    for i in count:
        if i == 1:
            break
        index +=1
    print(uniq[index])
'''
