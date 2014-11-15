def f(test='92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19'):
    test = test.strip().split(',')
    d = {}
    for num in test:
        d[num] = d.get(num,0) + 1
    for k,v in d.items():
        if v > len(test) / 2:
            print(k)
            break
    else:
        print("None")
