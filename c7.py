import operator
def f(test='* + 2 3 4\n'):#20... (2 + 3) * 4
    test = test.rstrip('\n').split()
    index = len(test) // 2
    summ = [int(test[index])]
    for j in range(index+1, len(test)):
        op = test[index-j+index]
        if op == '+':
            op = operator.add
        elif op == '*':
            op = operator.mul
        else:
            op = operator.truediv
        summ = list(map(op, summ, [int(test[j])] ))
    print(summ[0])
