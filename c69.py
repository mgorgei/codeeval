def f(test='rabbbit,rabbit'):#3
    string,pattern = test.rstrip('\n').split(',')
    print(g(string, pattern))
    
def g(string, pattern):
    if not pattern:
        return 1
    count = 0
    while pattern[0] in string:
        string = string[string.index(pattern[0]) + 1:]
        count+= g(string, pattern[1:])
    return count
