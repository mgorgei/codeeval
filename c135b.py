def f(test='s1s,s2s,s3s,s4s'):
    chain = test.rstrip().split(',')
    high = 0
    for i in range(len(chain)):
        temp = g([chain[i]], chain[:i] + chain[i+1:])
        if temp > high:
            high = temp
    if high > 1:
        print(high)
    else:
        print('None')

def g(link, chain):
    if chain == "":
        return len(link)
    highest = 0
    for i in range(len(chain)):
        if link[-1][-1] == chain[i][0]:
            stink = link[:]
            stink.append( chain[i] )
            temp = g(stink[:], chain[:i] + chain[i+1:])
            if temp > highest:
                highest = temp
    return max(len(link),highest)
