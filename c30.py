def f(test='7,8,9;8,9,10,11,12'):
    test = test.strip().split(';')
    test[0] = test[0].split(',')
    test[1] = test[1].split(',')
    result = ""
    for i in test[0]:
        if i in test[1]:
            result+=i+','
    print(result[:-1])
