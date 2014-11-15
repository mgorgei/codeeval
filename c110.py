ones = ['one','two','three','four','five','six','seven','eight','nine']
tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
enty = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def f(test='negative nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine'):
    test = test.rstrip().split()
    if 'zero' == test[0]:
        print('0')
        return #break
    base = ['+','000','000','000']
    case = [' ',[   ],[   ],[   ]]
    if 'negative' in test:
        base[0] = '-'
        test.remove('negative')
    if 'million' in test:
        case[1] = test[:test.index('million')]
        test = test[test.index('million') + 1:]
    if 'thousand' in test:
        case[2] = test[:test.index('thousand')]
        test = test[test.index('thousand') + 1:]
    case[3] = test
    for i in range(1,4):#([1-9] [hundred]) ([tens] [ones]) or [10-19]
        if not case[i]:
            continue
        hundreds = -1
        if 'hundred' in case[i]:
            hundreds = case[i].index('hundred')
        if hundreds != -1:
            base[i] += str(ones.index(case[i][0]) + 1)
            case[i] = case[i][hundreds + 1:]
        if case[i]:#need to process tens
            for j in range(len(tens)):
                if case[i][0] == tens[j]:
                    base[i]+= '1' + str(j)
                    break
            else:
                noenty = False
                for j in range(len(enty)):
                    if case[i][0] == enty[j]:
                        base[i]+= str(2+j)
                        case[i].pop(0)
                        if not case[i]:
                            base[i]+= '0'
                        break
                else:
                    noenty = True
                if case[i]:
                    for j in range(len(ones)):
                        if case[i][0] == ones[j]:
                            base[i]+= (noenty*'0') + str(1+j)
                            break
        else:
            base[i]+= '00'
        base[i] = base[i][-3:]
    result = "".join(base)
    for i in range(1,len(result)):
        if result[i] != '0':
            result = result[0] + result[i:]
            break
    print(eval(result))
