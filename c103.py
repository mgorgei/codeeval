def f(test='9 2 9 9 1 8 8 8 2 1 1'):
    test = test.strip().split()
    uniq = []
    repeat = []
    for digit in test:
        if not int(digit) in uniq:
            uniq.append(int(digit))
        else:
            repeat.append(int(digit))
    sorteduniq = sorted(uniq)
    for digit in sorteduniq:
        if not int(digit) in repeat:
            print(test.index(str(digit))+1)
            break
    else:
        print(0)
