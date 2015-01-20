'''FLAVIUS JOSEPHUS

Flavius Josephus was a famous Jewish historian of the first century, at the time
of the destruction of the Second Temple. According to legend, during the
Jewish-Roman war he was trapped in a cave with a group of soldiers surrounded by
Romans. Preferring death to capture, the Jews decided to form a circle and,
proceeding around it, to kill every j'th person remaining until no one was left.
Josephus found the safe spot in the circle and thus stayed alive. 

Write a program that returns a list of n people, numbered from 0 to n-1, in the
order in which they are executed.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains two comma separated positive integers n and m, where n is
the number of people and every m'th person will be executed. E.g.

10,3
5,2

OUTPUT SAMPLE:
Print out the list of n people (space delimited) in the order in which they will
be executed. E.g.

2 5 8 1 6 0 7 4 9 3
1 3 0 4 2
'''
from collections import deque
def f(test='10,3'):
    test = test.rstrip().split(',')
    people = deque( range(int(test[0])) )
    result = ""
    while len(people):
        people.rotate(-int(test[1])+ 1)
        result += str(people.popleft()) + ' '
    print(result[:-1])
