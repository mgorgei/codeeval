def f(test='1234'):
    test = test.rstrip()
    count = 1
    if len(test) == 1:
        return count
    valid=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    value=[0,0,0]
    fibo = 0
    unlocked = True
    single = test[-1]
    #need to model 1319 and 1718 => 4 instead of 3...
    for ten in reversed(test[:-1]):
        value[0] = int(ten + single)
        value[1] = int(ten)
        value[2] = int(single)
        if sum((value[i] in valid for i in range(3) )) == 3:#capable of two
            count += unlocked * fibonacci(fibo)
            if unlocked:
                fibo += 1
        else:
            fibo = 0
        unlocked = True
        if single == '0':
            unlocked = False
        single = ten
    return count



















def f1(test='1234'):
    test = test.rstrip()
    count = 1
    if len(test) == 1:
        return count
    unbound = True#need to sandbag a value if the preceding one forces a choice
    Prbound = True
    valid=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    value=[0,0,0]
    fibo = 0
    bind = 0
    prevchar = test[-1]
    for char in reversed(test[:-1]):
        value[0] = int(char + prevchar)
        value[1] = int(char)
        value[2] = int(prevchar)
        if sum((value[i] in valid for i in range(3) )) == 3:#capable of two
            #need to model consecutive '1' or '2' to match fibonacci sequence...
            #2=>2 3=>3 4=>5 5=>8
            count += Prbound * fibonacci(fibo)
            if Prbound:
                fibo+= 1
            else:
                fibo = 0
            '''if fibo > 1:
                unbound = Prbound
            else:
                unbound = not Prbound'''
            if not bind:
                unbound = True
        else:
            fibo = 0
        #check for binding
        if prevchar == '0':#value is 10 / 20 only
            unbound = False
        prevchar = char
        Prbound = unbound
        if bind == 1:
            unbound = True
        bind = bind - 1
    return count

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
