'''JUSTIFY THE TEXT

Write a program that reformats the text into lines of 80 symbols by stretching
the text to full line width by adding extra spaces.

Longer series of spaces should go first. For example:

if you need to add just one extra space, add it between the first and the second
word
if there are 4 words in a line, and you need 10 spaces to stretch the text up to
80 symbols, add 4 spaces between the first and the second word, 3 spaces between
the second and the third word, and 3 spaces between the third and the fourth
word.
The last line of the paragraph remains unchanged.

INPUT SAMPLE:
The first argument is a filename. The input file contains a text.
For example:

Hello, World!
The precise 50-digits value of Pi is 3.14159265358979323846264338327950288419716939937510.
But he who would be a great man ought to regard, not himself or his interests, but what is just, whether the just act be his own or that of another. Next as to habitations. Such is the tradition.

OUTPUT SAMPLE:
Print to stdout the text, reformatted into lines of 80 symbols by stretching the
text to the full line width by adding extra spaces.
For example:

Hello, World!
The         precise         50-digits        value        of        Pi        is
3.14159265358979323846264338327950288419716939937510.
But  he  who would be a great man ought to regard, not himself or his interests,
but what is just, whether the just act be his own or that of another. Next as to
habitations. Such is the tradition.
'''
MAXCHARS = 80
def f(test='But he who would be a great man ought to regard, not himself or his interests, but what is just, whether the just act be his own or that of another. Next as to habitations. Such is the tradition.'):
    test = test.rstrip('\n')
    split = []
    while test:
        if len(test) > MAXCHARS:
            if test[MAXCHARS] == ' ':
                split.append(test[:MAXCHARS].split())
                test = test[MAXCHARS + 1:]
            else:
                index = test.rfind(' ', 0, MAXCHARS)
                split.append(test[:index].split())
                test = test[index + 1:]
        else:
            split.append(test.split())
            test = ""
    output = ''
    for i in range(len(split) - 1):
        length = len(''.join(split[i]))
        spaces = MAXCHARS - length
        gaps = len(split[i]) - 1
        spaces_used = spaces // gaps
        remainder = spaces - gaps * spaces_used
        for s in range(len(split[i]) - 1):
            output+= split[i][s] + (' ' * spaces_used) + (' ' if remainder else '')
            if remainder:
                remainder -= 1
        output+= split[i][-1] + '\n'
    output+= ' '.join(split[-1])
    print(output)
