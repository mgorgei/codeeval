def f(s='sample.txt'):
    test_cases = open(s)
    result = 0
    lastpos = 0
    master = []
    for test in test_cases:
        test = [int(x) for x in test.split()]
        master.append(test)
    #have now converted file into list of lists of ints
    for i in range(len(master) - 2, -1, -1):
        for j in range(len(master[i])):
            master[i][j]+= max(master[i+1][j],master[i+1][j+1])
    return master[0][0]



def f1(s):
    test_cases = open(s)
    result = 0
    lastpos = 0
    master = []
    for test in test_cases:
        test = [int(x) for x in test.split()]
        master.append(test)
        if result != 0:
            result += max(test[lastpos], test[lastpos+1])
        else:
            result = test[lastpos] #head node
            continue
        print(test, test[lastpos], test[lastpos+1])
        if test[lastpos+1] > test[lastpos]:
            lastpos+=1
    return master
#need to find max value from one traversal... not max at each individual turn
#tree is depth 100...

def f2(s):
    test_cases = open(s)
    result = 0
    lastpos = 0
    master = []
    for test in test_cases:
        test = [int(x) for x in test.split()]
        master.append(test)
    #have now converted file into list of lists of ints
    #brute = [False for i in range(100)]#10000 traversals
    brute = 0
    mask = 0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    lastpos = 0
    temp = 0
    max = 0
    return master
    for rotations in range(10000):
        for i in range(100):
            lastpos+=brute[i]
            if temp > max:
                max = temp
        
    #if value already true, flip it, assess next index
    #0 1 10 11 100 101 110
