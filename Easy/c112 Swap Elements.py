'''SWAP ELEMENTS

You are given a list of numbers which is supplemented with positions that have
to be swapped.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following
1 2 3 4 5 6 7 8 9 : 0-8
1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3
As you can see a colon separates numbers with positions. 
Positions start with 0. 
You have to process positions left to right. In the example above (2nd line)
first you process 0-1, then 1-3.

OUTPUT SAMPLE:
Print the lists in the following way.
9 2 3 4 5 6 7 8 1
2 4 3 1 5 6 7 8 9 10
'''
def f(test="1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3"):
    test = test.split(':')
    test[0] = test[0].split()
    test[1] = test[1].split(',')
    for swap in test[1]:
        swap = swap.strip().split('-')
        test[0][int(swap[0])], test[0][int(swap[1])] = test[0][int(swap[1])], test[0][int(swap[0])]
    result = ""
    for out in test[0]:
        result += out + ' '
    print(result[:-1])
