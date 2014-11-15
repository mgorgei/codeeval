def f(test='4-2;BEGIN-3;3-4;2-END'):
    test = test.rstrip().split(';')
    chain = ['']#[''] * len(test)
    for c in test:
        if 'BEGIN-' in c:
            chain[0] = c
            test.remove(c)
            break
        '''if '-END' in c:
            chain[-1] = c
            '''
    for i in range(len(test)):#-1 ???
        nextrung = chain[i][chain[i].index('-')+1:]
        for j in range(len(test)):
            if test[j][:test[j].index('-')] == nextrung:#probably need to check for -END in case of dupes
                chain.insert(i+1, test[j])
                test.remove(test[j])
                break
        else:
            return 'BAD'
            break
    #print(chain)
    if chain[0].find('BEGIN-') != -1 and chain[-1].find('-END') != -1:
        return 'GOOD'
    else:
        return 'BAD'
