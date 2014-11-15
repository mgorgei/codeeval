def f(test='yellow'):
    test = test.rstrip()
    uniq = []
    count = []
    for char in test:
        if not char in uniq:
            uniq.append(char)
            count.append(1)
        else:
            count[uniq.index(char)]+= 1
    index = 0
    for i in count:
        if i == 1:
            break
        index +=1
    print(uniq[index])
