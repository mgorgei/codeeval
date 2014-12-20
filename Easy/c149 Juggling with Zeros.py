'''JUGGLING WITH ZEROS

In this challenge, you will deal with zero-based numbers. A zero-based number
has the following form: "flag" "sequence of zeroes" "flag" "sequence of zeroes",
and so on. The numbers are separated by a single space.

00 0 0 00 00 0
You have to convert zero-based numbers into integers. To do this, you need to
perform the following steps:

Convert a zero-based number into a binary form using the following rules:
a) flag "0" means that the following sequence of zeroes should be appended to a
binary string.

b) flag "00" means that the following sequence of zeroes should be transformed
into a sequence of ones and be appended to a binary string.

00 0 0 00 00 0 --> 1001
Convert the obtained binary string into an integer.
1001 --> 9

INPUT SAMPLE:
The first argument is a file where each line of input contains a string with
zero-based number.
For example:
00 0 0 00 00 0
00 0
00 0 0 000 00 0000000 0 000
0 000000000 00 00

OUTPUT SAMPLE:
For each line of input, print an integer converted from a zero-based number.
For example:
9
1
9208
3
'''
def f(test="00 0 0 00 00 0"):
    result = ""
    test = test.split()
    for i in range(0, len(test), 2):
        result+= ('0' if test[i]=='0' else '1') * len(test[i+1])
    return int(result, 2)
