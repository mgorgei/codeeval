import itertools
def f(test):
    test = test.rstrip().split(',')
    test[1] = set(test[1])
    result = ''
    x = itertools.product(test[1],repeat=int(test[0]))
    x = sorted(x)
    for i in x:
        result+= ''.join(i) + ','
    print(result[:-1])
