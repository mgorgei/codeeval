#permutation combination recursion regular expression
import re
def f(test='12345'):
    test = test.rstrip()
    ugly_prime = (2, 3, 5, 7)
    count = 0
    candidates = []
    g(test[0], test[1:], candidates)
    for i in range(len(candidates)):
        candidates[i] = eval(candidates[i])
    for number in candidates:
        for ugly in ugly_prime:
            if number % ugly == 0:
                count+=1
                break
    print(count)

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
        return combo
    plusminus = []
    for i in range(len(combo)):
        if combo[i] == '+' or combo[i] == '-':
            plusminus.append(combo[i])
    copy = re.split("[+\-]*", combo)
    result = ''
    for c in copy:
        if c != '0':
            result+= c.lstrip('0') + (plusminus.pop(0) if plusminus != [] else '')
        else:
            result+= c + (plusminus.pop(0) if plusminus != [] else '')
    return result
