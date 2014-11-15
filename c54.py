def f(test='15.94;16.00'):
    test = [float(x) for x in test.rstrip().split(';')]
    purchase_price = test[0]
    cash = test[1]
    if cash < purchase_price:
        return 'ERROR'
    if cash == purchase_price:
        return 'ZERO'
    result = ""
    change = round(cash - purchase_price, 2)
    words = ['ONE HUNDRED', 'FIFTY', 'TWENTY', 'TEN', 'FIVE', 'TWO', 'ONE',
             'HALF DOLLAR', 'QUARTER', 'DIME', 'NICKEL', 'PENNY']
    value = [100.0,50.0,20.0,10.0,5.0,2.0,1.0,.50,.25,.1,.05,.01]
    while change > 0.00:
        for ch in range(len(words)):
            if change >= value[ch]:
                result += words[ch] + ','
                change = round(change - value[ch], 2)
                break
    print(result[:-1])
