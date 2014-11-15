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
