def f(test='3 1'):
    test = test.split()
    locked = [False for i in range(int(test[0]))]
    for iteration in range( int(test[1]) - 1 ):
        for i in range(int(test[0])):
            if i % 2 == 1:
                locked[i] = True
            if i % 3 == 2:
                locked[i] = not locked[i]
    locked[-1] = not locked[-1]
    return sum(not y for y in locked)
