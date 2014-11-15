def f(string='text (:()'):#YES
    candidates = []
    g(string, candidates)
    for s in candidates:
        paren = ''
        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                paren+= s[i]
        if balanced(paren):
            print('YES')
            return
    else:
        print('NO')
        
def g(string, candidates):
    frowny, smiley = string.find(':('), string.find(':)')
    if frowny == -1 and smiley == -1:
        candidates.append(string)
        return
    face = -1
    if frowny != -1 and smiley != -1:
        face = min(frowny, smiley)
    elif frowny != -1 or smiley != -1:
        face = max(frowny, smiley)
    #interpret nearest smiley as smiley or parenthesis
    if face != -1:
        g(string[:face] + string[face+2:], candidates)#skip smiley
        g(string[:face] + string[face+1:], candidates)
    else:
        print('impossible')

def balanced(string):
    while string:
        paren = string.find(')')
        if paren == 0:
            return False
        if paren == -1:
            if string.find('(') != -1:
                return False
            paren = len(string)
        if string[paren -1] != '(':
            return False
        else:
            string = string[:paren-1] + string[paren+1:]
    return True
