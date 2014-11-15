from itertools import permutations
def f(test):
    print(','.join( [''.join(item) for item in sorted(permutations(test.rstrip('\n')))] ))
