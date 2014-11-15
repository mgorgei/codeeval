def f(test="00 0 0 00 00 0"):
    result = ""
    test = test.split()
    for i in range(0, len(test), 2):
        result+= ('0' if test[i]=='0' else '1') * len(test[i+1])
    return int(result, 2)
