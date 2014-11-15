def f(test='7 7 7'):
    test = test.strip().split()
    test = [int(x) for x in test]
    lastdigit = -1
    count = 0
    result = ""
    for digit in test:
        if digit == lastdigit:
            count+=1
        else:
            if lastdigit != -1:
                result+= str(count) + ' ' + str(lastdigit) + ' '
            lastdigit = digit
            count = 1
    result+= str(count) + ' ' + str(lastdigit)
    print(result)
