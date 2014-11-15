def f(test='Hello,lloHe'):
    test = test.rstrip().split(',')
    if len(test[0]) != len(test[1]):
        return False
    for i in range(len(test[0])):
        if test[0] == (test[1][i:] + test[1][:i]):
            return True
    return False
