def f(test='a b c d 4\n'):
    test = test.rstrip().split()
    index = int(test[-1])
    if index < len(test):
        print(test[-(index+1)])
