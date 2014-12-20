'''Prime Palindrome

Write a program which determines the largest prime palindrome less than 1000.

INPUT SAMPLE:
There is no input for this program.

OUTPUT SAMPLE:
Print to stdout the largest prime palindrome less than 1000.

929
'''
def isPrime(number):  
    if number <= 1:
        return False
    for check in range(2, number):
        if (number % check) == 0:
            return False
    return True

def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i-1]:
            return False
    return True

def f():
    for i in range(1001, 0,-1):
        if isPalindrome(str(i)):
            if isPrime(i):
                print(i)
                return
