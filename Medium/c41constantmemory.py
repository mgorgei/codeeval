def f(test='5;0,1,1,2,3'):
    size = int(test[:test.index(';')])
    test = test[test.index(';') + 1:].rstrip().split(',')
    test = [int(x) for x in test]
    test.append(77)
    for i in range(size):
        if test[abs(test[i])] >= 0:
            if test[abs(test[i])] == 0:
                if test[size] > 0:
                    test[abs(test[i])] = -size
                else:
                    print(0)
                    break
            else:
                test[abs(test[i])] = -test[abs(test[i])]
        else:
            print(abs(test[i]))
            break
    else:
        print('no')
