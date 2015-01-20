'''UGLY NUMBERS

Credits: This challenge has appeared in a google competition before.
Once upon a time in a strange situation, people called a number ugly if it was
divisible by any of the one-digit primes (2, 3, 5 or 7). Thus, 14 is ugly, but
13 is fine. 39 is ugly, but 121 is not. Note that 0 is ugly. Also note that
negative numbers can also be ugly: -14 and -39 are examples of such numbers.

One day on your free time, you are gazing at a string of digits, something like:

123456
You are amused by how many possibilities there are if you are allowed to insert
plus or minus signs between the digits. For example you can make: 

1 + 234 - 5 + 6 = 236
which is ugly. Or

123 + 4 - 56 = 71
which is not ugly. 

It is easy to count the number of different ways you can play with the digits:
Between each two adjacent digits you may choose put a plus sign, a minus sign,
or nothing. Therefore, if you start with D digits there are 3^(D-1) expressions
you can make. Note that it is fine to have leading zeros for a number. If the
string is '01023', then '01023', '0+1-02+3' and '01-023' are legal expressions.

Your task is simple: Among the 3^(D-1) expressions, count how many of them
evaluate to an ugly number.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will be a single line containing a
non-empty string of decimal digits. The string in each test case will be
non-empty and will contain only characters '0' through '9'. Each string is no
more than 13 characters long. E.g.

1
9
011
12345

OUTPUT SAMPLE:
Print out the number of expressions that evaluate to an ugly number for each
test case, each one on a new line. E.g.

0
1
6
64
'''
#permutation combination recursion regular expression
import re
import time
def f(test='12345'):
    start = time.time()
    test = test.rstrip()
    copy = test
    test = test.lstrip('0')
    if len(test) != len(copy):
        test = '0' + test
    ugly_prime = (2, 3, 5, 7)
    count = 0
    candidates = []
    g(test[0], test[1:], candidates)
    for number in candidates:
        for ugly in ugly_prime:
            if number % ugly == 0:
                count+=1
                break
    print(time.time() - start)
    #cheap shortcut out of leading zero runtime
    print(count * pow(3 , (len(copy) - len(test)) ))
    
def g(combo, test, result):
    if test == '':
        result.append( h(combo) )
    else:
        if combo[-1] != '+' and combo[-1] != '-':
            g(combo + '+', test, result)
            g(combo + '-', test, result)
        g(combo + test[0], test[1:], result)

def h(combo):
    if len(combo) == 1:
        return int(combo)
    plusminus = []
    for i in range(len(combo)):
        if combo[i] == '+' or combo[i] == '-':
            plusminus.append( (combo[i]) )
    copy = re.split("[+\-]*", combo)
    for i in range(len(copy)):
        if copy[i] != '0':
            copy[i] = copy[i].lstrip('0')
            if not copy[i]:
                copy[i] = '0'
    result = int(copy[0])
    for i in range(1,len(copy)):
        if plusminus.pop(0) == '-':
            result+= int(copy[i])
        else:
            result-= int(copy[i])
    return result
