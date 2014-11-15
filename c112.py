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
