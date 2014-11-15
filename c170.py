from math import ceil
from math import floor
def f(test='100 Lower Lower Higher Lower Lower Lower Yay!\n'):#5...8...7
    #0123456789
    number, *responses = test.rstrip('\n').split()
    number = int(number)
    lower = 0
    upper = number
    guess = ceil((upper + lower) / 2)
    for response in responses:
        print(guess, upper, lower)
        if response == 'Yay!':
            print(guess)
            break#not needed?
        elif response == 'Lower':
            upper = guess - 1
        elif response == 'Higher':
            lower = guess + 1
        guess = ceil((upper + lower) / 2)
    #0-n inclusive
'''
100 Lower Lower Higher Lower Lower Lower Yay!
948 Higher Lower Yay!
0 9 9/2 == 4.5 ceil == 5 (higher-> lower == guess+1....
6 9 15/2 == 7.5 ceil == 8 (lower-> higher == guess-1
6 7 13/2 == 6.5 ceil == 7 end
'''
