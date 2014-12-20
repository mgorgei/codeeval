'''UNIQUE ELEMENTS
You are given a sorted list of numbers with duplicates. Print out the sorted
list with duplicates removed.

INPUT SAMPLE:
File containing a list of sorted integers, comma delimited, one per line. E.g. 

1,1,1,2,2,3,3,4,4
2,3,4,5,5

OUTPUT SAMPLE:
Print out the sorted list with duplicates removed, one per line. E.g.

1,2,3,4
2,3,4,5
'''
def f(test='1,1,1,2,2,3,3,4,4'):
    test = test.rstrip().split(',')
    unique = []
    for n in test:
        if n not in unique:
            unique.append(n)
    print(','.join(unique))
