def f(test='22 2 2 9 11', pole=6):
    test = test.rstrip().split()
    length = int(test[0])
    distance = int(test[1])
    n = int(test[2])
    bats = [int(x) for x in test[3:]] if n else []
    bats = sorted(bats)
    left = pole
    right = length - pole
    if bats:
        if left < bats[0] - distance:
            bats.insert(0,left)
    else:
        bats.insert(0,left)
    index = 0
    bound = 0
    while True:
        if index + 1 < len(bats):
            bound = bats[index+1]
        else:
            bound = right
        if bats[index] + distance <= bound - distance:
            bats.append(bats[index] + distance)
            bats.sort()
        index+=1
        if index >= len(bats):
            break
    while bats[-1] + distance <= right:
        bats.append(bats[-1] + distance)
    return len(bats) - n
