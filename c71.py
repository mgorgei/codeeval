def f(test='1,2,3,4,5;2'):
    test = test.rstrip().split(';')
    sequence = test[0].split(',')
    length = int(test[1])
    result = ""
    for index in range(0, len(sequence), length):
        if index + length > len(sequence):
            result+= ','.join(sequence[index:]) + 'X'
            break
        for reverse in range(index + length - 1, index - 1, -1):
            result+= sequence[reverse] + ','
    print(result[:-1])
