def f(test):
    test = test.split('|')
    test[0] = str(test[0]).split()
    test[1] = str(test[1]).split()
    zipped = zip(test[0], test[1])
    result = ""
    for x,y in zipped:
        result += str(int(x)*int(y)) + ' '
    print(result)
    #9 0 6 | 15 14 9
