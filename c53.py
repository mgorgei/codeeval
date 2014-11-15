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
