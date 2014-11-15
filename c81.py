from itertools import combinations

def f(test='2,3,1,0,-4,-1\n'):
    test = [int(x) for x in test.rstrip().split(',')]
    test = list(combinations(test, 4))
    count = 0
    for item in test:
        res = ''
        for i in range(4):
            res+=str(item[i])+'+'
        if eval(res[:-1]) == 0:
            count+=1
    print(count)
