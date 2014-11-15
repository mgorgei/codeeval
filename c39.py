"""A happy number is the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers, while those that do not end in 1 are
unhappy numbers.
"""
def f(test='7'):
    test = test.strip()
    uniq = [int(test)]
    while int(test) != 1:
        rep = 0
        for digit in test:
            rep += int(digit)* int(digit)
        test = str(rep)
        if not int(test) in uniq:
            uniq.append(int(test))
        else:
            print('0')
            break
    else:
        print('1')
