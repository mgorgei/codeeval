def f(s):
    s = s.split(',')
    s = [int(x) for x in s]
    return (s[0] <= s[6] and s[2] >= s[4] and s[1] >= s[7] and s[3] <= s[5])
