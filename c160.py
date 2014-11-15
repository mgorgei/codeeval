def f(test='330.39991833'):
    test = float(test.strip())
    a = int(test)
    b = (test - a) * 60
    c = (b - int(b)) * 60
    print("{0}.{1:02}'{2:02}\"".format(a,int(b),int(c)))
