'''REPEATED SUBSTRING

You are to find the longest repeated substring in a given text. Repeated
substrings may not overlap. If more than one substring is repeated with the same
length, print the first one you find.(starting from the beginning of the text). 
NOTE: The substrings can't be all spaces.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. The input
file contains several lines. Each line is one test case. Each line contains a
test string. E.g.

banana
am so uniqe

OUTPUT SAMPLE:
For each set of input produce a single line of output which is the longest
repeated substring. If there is none, print out the string NONE. E.g.

an
NONE
'''
def f(test='banana'):
    string = test.rstrip('\n')
    for i in range(len(string)-1,0,-1):
        for j in range(len(string) - i):
            if string[j:i+j] in string[j+i:] and string[j:i+j].count('  ') == 0 and string[j:i+j]!=' ':
                return string[j:i+j]
    return 'NONE'
'''
banana (cannot do original because it doesn't repeat)
banan anana
bana anan nana
ban ana nan ana
ba an na an na
b a n a n a
'''
