def f(test='soup,sugar,peas,rice'):
    chain = test.rstrip().split(',')
    cur_count = 0
    count = 0
    for i in range( (len(chain)) - 2 ):
        if chain[i][-1] == chain[i + 2][0]:
            cur_count += 2
        else:
            cur_count = 0
        if cur_count > count:
            count = cur_count
    if count == 0:
        print(None)
    else:
        print(count)
