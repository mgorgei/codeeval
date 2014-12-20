'''COMPRESSED SEQUENCE

Assume that someone dictates you a sequence of numbers and you need to write it
down. For brevity, he dictates it as follows: first says the number of
consecutive identical numbers and then says the number itself. E.g. The sequence
1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2 will be dictated as
"Two times one, three times three, four times two, three times fourteen, three times eleven, one timetwo",
so you will write down the sequence 2 1 3 3 4 2 3 14 3 11 1 2. The challenge is
to write the program which compresses the given sequence using this approach.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. The input
file contains T lines. Each line is a test case represented by a sequence of
integers L, where each integer is N, separated by a whitespace. E.g
40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86 86 86
86 86 86 86 86
73 73 73 73 41 41 41 41 41 41 41 41 41 41
1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2
7

OUTPUT SAMPLE:
For each test case produce a single line of output containing a compressed
sequence of numbers separated by a single space char. E.g.
4 40 8 29 2 57 5 92 10 86
4 73 10 41
2 1 3 3 4 2 3 14 3 11 1 2
1 7
'''
def f(test='7 7 7'):
    test = test.strip().split()
    test = [int(x) for x in test]
    lastdigit = -1
    count = 0
    result = ""
    for digit in test:
        if digit == lastdigit:
            count+=1
        else:
            if lastdigit != -1:
                result+= str(count) + ' ' + str(lastdigit) + ' '
            lastdigit = digit
            count = 1
    result+= str(count) + ' ' + str(lastdigit)
    print(result)
