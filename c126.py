def f(test='CCC 1 CGCCCGAATCCAG'):
    pattern, mismatch, string = test.split()
    matches = []
    for i in range(len(string)):
        temp = string[i:i+len(pattern)]
        if len(temp) != len(pattern):
            break
        result = is_match(pattern,temp,int(mismatch))
        if result[0]:
            matches.append( (string[i:i+len(pattern)], -result[1]) )
    if matches:
        print(' '.join( [y[0] for y in sorted( matches, key=lambda x: (x[1],x[0]) )] ))
    else:
        print('No match')
                   
def is_match(pattern, string, mismatch):
    for i in range(len(pattern)):
        if pattern[i] != string[i]:
            mismatch-=1
        if mismatch < 0:
            return (False, 0)
    return (True, mismatch)
