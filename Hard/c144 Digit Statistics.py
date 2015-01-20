'''DIGIT STATISTICS

Given the numbers "a" and "n" find out how many times each digit from zero to
nine is the last digit of the number in a sequence [ a, a2, a3, ... an-1, an ]

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
of input contains two space separated integers "a" and "n" E.g: 

2 5

OUTPUT SAMPLE:
For each line of input print out how many times the digits zero, one, two ...
nine occur as the last digit of numbers in the sequence E.g:

10: 0, 1: 0, 2: 2, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 1, 9: 0

In this example, the sequence consists of numbers 2, 4, 8, 16 and 32. Among the
last digits, the digit two occurs twice, and each of the digits four, six and
eight occurs once.
'''
def f(test='2 5'):
    a, n = test.rstrip('\n').split(' ')
    a = int(a) - 2
    n = int(n)
    digits = [0,0,0,0,0,0,0,0,0,0]
    pattern = [[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
    copies = n // len(pattern[a])
    for i in range(len(pattern[a])):
        digits[pattern[a][i]] = copies
    remainder = n % len(pattern[a]) 
    for i in range(remainder):
        digits[pattern[a][i]] += 1
    result = ''
    for i in range(10):
        result+= str(i) + ': {}, '.format(digits[i])
    print(result[:-2])
