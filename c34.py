from itertools import combinations
def f(test='2,4,5,6,9,11,15;20'):
    test = test.rstrip().split(';')
    test[0] = [int(x) for x in test[0].split(',')]
    test[1] = int(test[1])
    combo = combinations(test[0],2)
    result = ""
    for pair in combo:
        if pair[0] + pair[1] == test[1]:
            result+= str(pair[0]) + ',' + str(pair[1]) + ';'
    if result == "":
        print(NULL)
    else:
        print(result[:-1])
