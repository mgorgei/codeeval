def f(test='2 0 6 3 1 6 3 1 6 3 1'):#6 3 1
    test = test.rstrip('\n').split()
    for size in range(1, len(test) // 2 + 1):
        for index in range(len(test) - size + 1):
            print(size, index)
            print(test[index:index + size], test[index+size:index+size+size])
            if test[index:index + size] == test[index+size:index+size+size]:
                return ' '.join(test[index:index + size])
