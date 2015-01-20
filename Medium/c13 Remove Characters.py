'''REMOVE CHARACTERS

Write a program which removes specific characters from a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the source strings and
the characters that need to be scrubbed. Each source string and characters you
need to scrub are delimited by comma.

For example:

how are you, abc
hello world, def

OUTPUT SAMPLE:

Print to stdout the scrubbed strings, one per line. Ensure that there are no
trailing empty spaces on each line you print.

For example:

how re you
hllo worl
'''
def f(test="how are you, abc"):
    test = test.strip().split(',')
    result = test[0]
    test[1] = test[1].strip()
    for char in test[1]:
        result = result.replace(char, '')
    print(result)
