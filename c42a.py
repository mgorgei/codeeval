#permutation combination recursion regular expression
import re
import time
def f(test='12345'):
    start = time.time()
    test = test.rstrip()
    copy = test
    test = test.lstrip('0')
    if len(test) != len(copy):
        test = '0' + test
    ugly_prime = (2, 3, 5, 7)
    count = 0
    candidates = []
    g(test[0], test[1:], candidates)
    '''signs = [s for s in itertools.product(['+','-',''], repeat=len(test)-1)]
    for s in signs:
        s = list(s)
        number = test[0]
        for i in range(1, len(test)):
            number += s[i-1] + test[i]
        candidates.append(h(number))'''
    for number in candidates:
        for ugly in ugly_prime:
            if number % ugly == 0:
                count+=1
                break
    print(time.time() - start)
    #if len(test) != len(copy):
    #cheap shortcut out of leading zero runtime
    print(count * pow(3 , (len(copy) - len(test)) ))
    #else:
    #    print(count)

def g(combo, test, result):
    if test == '':
        result.append( h(combo) )
    else:
        if combo[-1] != '+' and combo[-1] != '-':
            g(combo + '+', test, result)
            g(combo + '-', test, result)
        g(combo + test[0], test[1:], result)

def h(combo):
    if len(combo) == 1:
        return int(combo)
    plusminus = []
    for i in range(len(combo)):
        if combo[i] == '+' or combo[i] == '-':
            plusminus.append( (combo[i]) )
    copy = re.split("[+\-]*", combo)
    for i in range(len(copy)):
        if copy[i] != '0':
            copy[i] = copy[i].lstrip('0')
            if not copy[i]:
                copy[i] = '0'
    result = int(copy[0])
    for i in range(1,len(copy)):
        if plusminus.pop(0) == '-':
            result+= int(copy[i])
        else:
            result-= int(copy[i])
    return result
