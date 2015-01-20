'''LONGEST LINES

Write a program which reads a file and prints to stdout the specified number of
the longest lines that are sorted based on their length in descending order.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument. The file
contains multiple lines. The first line indicates the number of lines you should
output, the other lines are of different length and are presented randomly. You
may assume that the input file is formatted correctly and the number in the
first line is a valid positive integer.

For example:

2
Hello World
CodeEval
Quick Fox
A
San Francisco

OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted by their
length in descending order.

For example:

San Francisco
Hello World
'''
def f(file='t2.txt'):
    F= open(file)
    lines = []
    lengths = []
    biggest = -1
    for line in F:
        if biggest == -1:
            biggest = int(line.rstrip())
        line = line.rstrip()
        lines.append(line)
        lengths.append(len(line))
    zipped = zip(lines, lengths)
    zipped = sorted(zipped, key=lambda x:x[1], reverse=True)
    x, y = zip(*zipped)
    result = ""
    for i in range(biggest):
        print(x[i])
