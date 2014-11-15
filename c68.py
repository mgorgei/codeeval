def f(test='([)]'):#False
    s = test.rstrip('\n')
    while s:
        parenthesis, bracket, brace = s.find(')'), s.find(']'), s.find('}')
        if parenthesis == -1:
            parenthesis = len(s)
        if bracket == -1:
            bracket = len(s)
        if brace == -1:
            brace = len(s)
        if parenthesis < bracket and parenthesis < brace:
            if s[parenthesis-1] != '(':
                break
            s = s[:parenthesis-1] + s[parenthesis+1:]
        elif  bracket < parenthesis and bracket < brace:
            if s[bracket-1] != '[':
                break
            s = s[:bracket-1] + s[bracket+1:]
        elif brace < parenthesis and brace < bracket:
            if s[brace-1] != '{':
                break
            s = s[:brace-1] + s[brace+1:]
        else:
            break
    if s:
        print(False)
    else:
        print(True)
