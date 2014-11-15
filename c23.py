def f():
    for i in range(1,13):
        line = ""
        for j in range(i, i*13, i):
            '''if j == i:
                line += str(j)
            else:'''
            line += ' ' *(4 - len(str(j))) + str(j)
        print(line)

'''
1   2   3   4   5   6   7   8   9  10  11  12
2   4   6   8  10  12  14  16  18  20  22  24
3   6   9  12  15  18  21  24  27  30  33  36
'''
