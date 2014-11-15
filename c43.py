def f(test='4 4 1 3 2'):
    test = [int(x) for x in test.rstrip().split()]
    jolly = [0]
    for i in range(1, len(test) -1):
        jolly.append(abs(test[i] - test[i+1]))
    if sorted(jolly) == list(range(len(test))):
        print('Jolly')
    else:
        print('Not jolly')
