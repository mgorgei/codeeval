import itertools
def f(test='842'):
    test = test.rstrip('\n')
    permutations = itertools.permutations('0' + test)
    lowest = int(test + '0')
    for permutation in permutations:
        p = int(''.join(permutation).lstrip('0'))
        if p > int(test) and p < lowest:
            lowest = p
    print(lowest)
