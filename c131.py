def f(test):
    test = test.split()
    index = max(test[1].find('-'), test[1].find('+'))
    exp = test[0][:index] + test[1][index] + str(int(test[0][index:]))
    print(eval(exp))
