def f(test='5;0,1,2,3,0'):
    size = int(test[:test.index(';')])
    test = test[test.index(';') + 1:].rstrip().split(',')
    test = [int(x) for x in test]
    uniq = []
    for elem in test:
        if not elem in uniq:
            uniq.append(elem)
        else:
            print(str(elem))
            break
