def f(s):
    s = s.split()
    x = int(s[0])
    y = int(s[1])
    n = int(s[2])
    result = ""
    for i in range(1,n+1):
        out = ""
        if i%x==0:
            out +="F"
        if i%y==0:
            out +="B"
        if out == "":
            out = str(i)
        result += out + ' '
    return result.rstrip()
