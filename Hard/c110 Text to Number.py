'''TEXT TO NUMBER

You have a sting which contains a number represented as English text. Your task
is to translate these numbers into their integer representation. The numbers can
range from negative 999,999,999 to positive 999,999,999. The following is an
exhaustive list of English words that your program must account for:

negative,
zero, one, two, three, four, five, six, seven, eight, nine,
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,
twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety,
hundred,
thousand,
million

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following

fifteen
negative six hundred thirty eight
zero
two million one hundred seven
- Negative numbers will be preceded by the word negative. 
- The word "hundred" is not used when "thousand" could be. E.g. 1500 is written
"one thousand five hundred", not "fifteen hundred".

OUTPUT SAMPLE:
Print results in the following way.

15
-638
0
2000107
'''
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
