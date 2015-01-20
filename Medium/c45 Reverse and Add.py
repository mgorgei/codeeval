'''REVERSE AND ADD

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla
The problem is as follows: choose a number, reverse its digits and add it to the
original. If the sum is not a palindrome (which means, it is not the same number
from left to right and right to left), repeat this procedure.

For example:

195 (initial number) + 591 (reverse of initial number) = 786

786 + 687 = 1473

1473 + 3741 = 5214

5214 + 4125 = 9339 (palindrome)

In this particular case the palindrome 9339 appeared after the 4th addition.
This method leads to palindromes in a few step for almost all of the integers.
But there are interesting exceptions. 196 is the first number for which no
palindrome has been found. It is not proven though, that there is no such a
palindrome.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain an integer n < 10,000.
Assume each test case will always have an answer and that it is computable with
less than 100 iterations (additions).

OUTPUT SAMPLE:
For each line of input, generate a line of output which is the number of
iterations (additions) to compute the palindrome and the resulting palindrome.
(they should be on one line and separated by a single space character).
For example:

4 9339
'''
def is_palindrome(s):     
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i-1]:
            return False
    return True

def f(test='195\n'):
    number = test.rstrip()
    for i in range(100):
        reverse = number[::-1]
        nsum = int(number) + int(reverse)
        if is_palindrome(str(nsum)):
            return "{} {}".format(str(i+1), str(nsum))
        number = str(nsum)
    return "fail"
