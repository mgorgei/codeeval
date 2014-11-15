def f(s):
    s = s.split("|")
    slist = s[0].split()
    slist = [int(digit) for digit in slist]
    fst = len(slist)
    iterations = int(s[1])
    while iterations:
        swap = False
        for i in range(fst-1):
            if slist[i] > slist[i+1]:
                swap = True
                slist[i], slist[i+1] = slist[i+1], slist[i]
        if swap == False:
            break
        iterations-=1
    result = ""
    for digit in slist:
        result += str(digit) + ' '
    return result[:-1]
