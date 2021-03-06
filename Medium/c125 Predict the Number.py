'''PREDICT THE NUMBER

Sequence 011212201220200112 ... constructed as follows: first is 0, then
repeated the following action: already written part is attributed to the right
with replacement 0 to 1, 1 to 2, 2 to 0. E.g.

0 -> 01 -> 0112 -> 01121220 -> ...
Create an algorithm which determines what number is on the N-th position in the
sequence.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains an integer N such as 
0 <= N <= 3000000000. E.g.

0
5
101
25684

OUTPUT SAMPLE:
Print out the number which is on the N-th position in the sequence. E.g.

0
2
1
0
'''
def f(test='50'):#0
    n = int(test.rstrip('\n'))
    patterns = ['0112', '1220', '2001']
    divisor = 4294967296
    pattern = patterns[0]
    while divisor > 1:
        div = n // divisor
        pattern = patterns[int(pattern[div])]
        n-= divisor * div
        divisor = divisor // 4
    return (pattern[n], pattern, n)

'''n = 50
 0     1     1     2
0-15 16-31 32-47 48-63
 0     1     2     3
 2   0   0     1
0-3 4-7 8-11 12-15
 0   1   2     3

 2 0 0 1
 0 1 2 3
0112122012202001122020012001011212202001200101122001011201121220 1
   A   B   B   C   B   C   C   A   B   C   C   A   C   A   A   B 4
               x               y               y               z 16
                                                               0 64
                                                                 256
                                                                 1024
                                                                 4096
                                                                 16384
                                                                 65536 (square > limit)
                                                                 262144
                                                                 1048576
                                                                 4194304
                                                                 16777216
                                                                 67108864
                                                                 268435456
0112                                                             1073741824
                                                                 4294967296 2^32
'''
'''xxx'''
'''011212201220200112
3,000,000,000

0 -> 01 -> 0112 -> 01121220 ->
0112122012202001 -> 01121220122020011220200120010112 ->
0112122012202001122020012001011212202001200101122001011201121220 ->
01121220122020011220200120010112122020012001011220010112011212201220200120010112200101120112122020010112011212200112122012202001
   4   8  12  16              32              48              64
0112A
1220B
1220B
2001C<
1220B
2001C
2001C
0112A<
1220B
2001C
2001C
0112A
2001C
0112A
0112A
1220B
1220B
2001C
2001C
0112A
2001C
0112A
0112A
1220B
2001C
0112A
0112A
1220B
0112A
1220B
1220B
2001C
---- ABBCBCCABCCACAABBCCACAABCAABABBC
ABBC0
BCCA1
BCCA1
CAAB2        D
BCCA1
CAAB2
CAAB2
ABBC0        E
CAAB2 ???
ABBC0
ABBC0
BCCA1        F

3 patterns 0112, 1220, 2001; A, B, C
'''
