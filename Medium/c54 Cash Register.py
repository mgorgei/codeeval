'''CASH REGISTER

The goal of this challenge is to design a cash register program. You will be
given two float numbers. The first is the purchase price (PP) of the item. The
second is the cash (CH) given by the customer. Your register currently has the
following bills/coins within it:

'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
The aim of the program is to calculate the change that has to be returned to the
customer.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. The input
file contains several lines. Each line is one test case. Each line contains two
numbers which are separated by a semicolon. The first is the Purchase price (PP)
and the second is the cash(CH) given by the customer. eg.

15.94;16.00
17;16
35;35
45;50

OUTPUT SAMPLE:
For each set of input produce a single line of output which is the change to be
returned to the customer. In case the CH < PP, print out ERROR. If CH == PP,
print out ZERO. For all other cases print the amount that needs to be returned,
in terms of the currency values provided. The output should be sorted in
highest-to-lowest order (DIME,NICKEL,PENNY). eg.

NICKEL,PENNY
ERROR
ZERO
FIVE
'''
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
