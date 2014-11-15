def f(test):
    for i in range(1,40):
        tempstr = test[0:i]
        for j in range(0,len(test), i):
            if tempstr != test[j:j+i]:
                break
        else:
            return i
    return i
