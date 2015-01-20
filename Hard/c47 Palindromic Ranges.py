'''PALINDROMIC RANGES

A positive integer is a palindrome if its decimal representation (without
leading zeros) is a palindromic string (a string that reads the same forwards
and backwards). For example, the numbers 5, 77, 363, 4884, 11111, 12121 and
349943 are palindromes. 

A range of integers is interesting if it contains an even number of palindromes.
The range [L, R], with L <= R, is defined as the sequence of integers from L to
R (inclusive): (L, L+1, L+2, ..., R-1, R). L and R are the range's first and
last numbers. 

The range [L1,R1] is a subrange of [L,R] if L <= L1 <= R1 <= R. Your job is to
determine how many interesting subranges of [L,R] there are.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain two positive
integers, L and R (in that order), separated by a space. eg. 

1 2
1 7
87 88

OUTPUT SAMPLE:
For each line of input, print out the number of interesting subranges of [L,R] eg. 

1
12
1

For the curious: In the third example, the subranges are: [87](0 palindromes),
[87,88](1 palindrome),[88](1 palindrome). Hence the number of interesting
palindromic ranges is 1
'''
def is_palindrome(s):     
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i-1]:
            return False
    return True
palindromes = []
truefalse = []
    
#find and record all palindromes in range L R; if count in L1;R1 is even ++
def f(test='1 7'):
    global palindromes
    global truefalse
    interesting = 0
    L, R = test.rstrip('\n').split()
    for i in range(int(L), int(R)+1):
        for j in range(i, int(R)+1):
            count = 0
            for number in range(i, j+1):
                if number in palindromes:
                    if truefalse[palindromes.index(number)]:
                        count+=1
                else:
                    palindromes.append(number)
                    truefalse.append(is_palindrome(str(number)))
                    if truefalse[palindromes.index(number)]:
                        count+=1
            if count % 2 == 0:
                interesting+=1
    print(interesting)
