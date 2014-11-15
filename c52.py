ones = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
tens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
enty = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
def f(test='3\n'):
    test = test.rstrip()
    base = ['','','']
    result = ['','','']
    base[2] = test[-3:]
    if len(test) > 6:
        base[0] = test[:len(test)-6]
        test = test[len(test)-6:]
    if len(test) > 3:
        base[1] = test[:len(test)-3]
    #['999','999','999']
    for i in range(3):
        if base[i]:
            if len(base[i]) > 2:
                if base[i][0] != '0':
                    result[i]+= ones[int(base[i][0])-1] + 'Hundred'
                base[i] = base[i][1:]
            if len(base[i]) > 1: #teen or enty
                if base[i][0] == '1':#teen
                    result[i]+= tens[int(base[i][1])]
                    base[i] = '0'
                else:#enty + (ones)
                    if base[i][0] != '0':
                        result[i]+= enty[int(base[i][0]) - 2]
                    base[i] = base[i][1]
            if base[i][0] != '0':
                result[i]+= ones[int(base[i][0])-1]
    if result[0]:
        result[0]+= "Million"
    if result[1]:
        result[1]+= "Thousand"
    result = ''.join(result)
    print(result + "Dollars")
