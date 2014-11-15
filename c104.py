def f(test):
    tr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    test = test.split(';')
    result = ""
    for digit in test:
        result += tr.index(digit)
    print(result)
