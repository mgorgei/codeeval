board = [[0 for _ in range(256)] for _ in range(256)]
def f(test):
    test = test.strip().split()

    if test[0] == "SetRow":
        for i in range(256):
            board[int(test[1])][i] = int(test[2])
    if test[0] == "SetCol":
        for j in range(256):
            board[j][int(test[1])] = int(test[2])
    if test[0] == "QueryRow":
        out = 0
        for i in range(256):
            out+= board[int(test[1])][i]
        print (out)
    if test[0] == "QueryCol":
        out = 0
        for j in range(256):
            out+= board[j][int(test[1])]
        print (out)
