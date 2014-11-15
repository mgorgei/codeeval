def f(test):
    test = test.strip().split(',')
    a = int(test[0])
    b = int(test[1])
    if a < b:
        print(a)
    else:
        x = b
        while(1):
            if b == 1:
                print(0)
                break
            elif a == x:
                print(0)
                break
            elif x + b <= a:
                x = x + b
            else:
                print(a - x)
                break
