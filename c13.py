def f(test="how are you, abc"):
    test = test.strip().split(',')
    result = test[0]
    test[1] = test[1].strip()
    for char in test[1]:
        result = result.replace(char, '')
    print(result)
