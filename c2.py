def f(file='t2.txt'):
    F= open(file)
    lines = []
    lengths = []
    biggest = -1
    for line in F:
        if biggest == -1:
            biggest = int(line.rstrip())
        line = line.rstrip()
        lines.append(line)
        lengths.append(len(line))
    zipped = zip(lines, lengths)
    zipped = sorted(zipped, key=lambda x:x[1], reverse=True)
    x, y = zip(*zipped)
    result = ""
    for i in range(biggest):
        print(x[i])
