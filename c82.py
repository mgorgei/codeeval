def f(test):
    test = test.strip()
    exp = ""
    for digit in test:
        exp+= digit + '**' + str(len(test)) + '+'
    x = eval(exp[:-1])
    print(x == int(test))
