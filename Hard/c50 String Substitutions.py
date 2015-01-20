'''STRING SUBSTITUTION

Credits: This challenge was contributed by Sam McCoy
Given a string S, and a list of strings of positive length, F1,R1,F2,R2,...,FN,RN,
proceed to find in order the occurrences (left-to-right) of Fi in S and replace
them with Ri. All strings are over alphabet { 0, 1 }. Searching should consider
only contiguous pieces of S that have not been subject to replacements on prior
iterations. An iteration of the algorithm should not write over any previous
replacement by the algorithm.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file is one test case. Each test case will contain a string, then a
semicolon and then a list of comma separated strings. E.g.

10011011001;0110,1001,1001,0,10,11

OUTPUT SAMPLE:
For each line of input, print out the string after substitutions have been made.eg.

11100110

For the curious, here are the transitions for the above example:
10011011001 => 10100111001 [replacing 0110 with 1001] => 10100110 [replacing
1001 with 0] => 11100110 [replacing 10 with 11]. So the answer is 11100110
'''
def f(test='10011011001;0110,1001,1001,0,10,11\n'):#11100110
    original, rest = test[:-1].split(';')
    mask = original[:]
    rest = rest.split(',')
    for i in range(0,len(rest),2):
        for bs in range(2):
            for j in range(len(original)):
                if rest[i] == original[j:j+len(rest[i])] == mask[j:j+len(rest[i])]:
                    original = original[:j] + rest[i+1] + original[j+len(rest[i]):]
                    mask = mask[:j] + len(rest[i+1]) * 'x' + mask[j+len(rest[i]):]
    print(original, mask)

'''s x s
10011011001 0110,1001
10100111001
10xxxx11001
10100111001 1001,0
10100110
10xxxx1x
10100110 10,11
11100110
xxxxxx1x
10100101101110011000 10,111
11111101111111111110111100
xxxxxx0xxx1xxx11xxx01xxx00
11111101111111111110111100 00,10
11111101111111111110111110
xxxxxx0xxx1xxx11xxx01xxxxx
11111101111111111110111110 010,00
xxxxxx0xxx1xxx11xxx01xxxxx
'''
