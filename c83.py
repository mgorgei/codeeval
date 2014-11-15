def f(test='ABbCcc'):
    test = test.strip().lower()
    uniq = []
    count = []
    for char in test:
        if char.isalpha():
            if not char in uniq:
                uniq.append(char)
                count.append(1)
            else:
                count[uniq.index(char)]+= 1
    zipped = zip(uniq,count)
    zipped = sorted(zipped, key=lambda x: x[1])
    zipped = reversed(zipped)
    sum = 0
    val = 26
    for x,y in zipped:
        sum += val*y
        val -= 1
    print(sum)
