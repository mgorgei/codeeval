def f(s):
    s = s.split(';')
    seq = s[0].split(' ')
    num = s[1].split(' ')
    num = [int(i) for i in num]
    for i in range(1, len(seq)+1):
        if not i in num:
            num.append(i)
    zipped = zip(seq,num)
    zipped = sorted(zipped, key=lambda x: x[1])
    result = ""
    for i in zipped:
        result += i[0] + ' '
    return result.rstrip()
