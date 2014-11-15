def f(test='http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html'):
    test = test.rstrip().split(';')
    for i in [0,1]:
        test[i] = test[i].lower()
        while test[i].find('%') != -1:
            index = test[i].index('%')
            try:
                char = chr(int(test[i][index+1:index+3],16))
                test[i] = test[i][:index] + char + test[i][index+3:]
            except:
                char = '!'
                test[i] = test[i][:index] + char + test[i][index+1:]
        index = test[i].find('://')
        pindex = test[i][index+3:].find(':')
        if pindex == -1:
            pindex = test[i][index+3:].find('/')
            test[i] = test[i][:index+pindex+3] + ':80' + test[i][index+pindex+3:]
            print(index, pindex)
    print(test[0], test[1])
    
    print(test[0] == test[1])
