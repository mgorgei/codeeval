def f(test):
    test = test.rstrip('\n').split()
    print('Yes') if g(test[0], test[1]) else print('No')

def g(seq, ab):
    if not seq:
        return ab == ''
    if seq and not ab:
        return False
    if seq[0] == '1':
        if ab[0] == 'A':
            count = 1
            while count < len(ab) and ab[count] == 'A':
                count+=1
            for i in range(count, 1, -1):
                if g(seq[1:], ab[i:]):
                    return True
            return g(seq[1:], ab[1:])
        else:
            count = 1
            while count < len(ab) and ab[count] == 'B':
                count+=1
            for i in range(count, 1, -1):
                if g(seq[1:], ab[i:]):
                    return True
            return g(seq[1:], ab[1:])
    else:
        if ab[0] == 'A':
            count = 1
            while count < len(ab) and ab[count] == 'A':
                count+=1
            for i in range(count, 1, -1):
                if g(seq[1:], ab[i:]):
                    return True
            return g(seq[1:], ab[1:])
        else:
            return False
