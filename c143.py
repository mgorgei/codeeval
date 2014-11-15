def f(test='Higher meaning;Hi mean'):
    test = test.rstrip('\n').split(';')
    utterance = test[0].split()
    utter = test[1].split()
    pair = []
    j = 0
    while utterance:
        if utter and utterance[0].find(utter[j]) != -1:
            pair.append( (utterance[0], utter[j]) )
            utterance.pop(0)
            utter.pop(j)
            j = 0
        else:
            if j + 1 < len(utter):
                j+=1
            else:
                pair.append( (utterance[0], '') )
                utterance.pop(0)
                j = 0
        '''if not utter:
            break'''
    if len(utter):
        print("I cannot fix history")
    else:
        result = ''
        for pr in pair:
            index = pr[0].find(pr[1])
            if index != -1:
                under = '_' * (len(pr[0]) - len(pr[1]))
                result += (under[:index] + pr[1] + under[index:]) + ' '
        print(result[:-1])
