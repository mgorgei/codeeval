def f(test='osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53'):
    test = test.strip('\n').split('|')
    positions = test[1].split()
    positions = [int(x) for x in positions]
    result = ""
    for pos in positions:
        result += test[0][pos-1]
    print(result)
