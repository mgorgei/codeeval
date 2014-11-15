def f(s):
    s = s.strip()
    lower = sum(char.islower() for char in s)
    return "lowercase: {:0.2f} uppercase: {:1.2f}".format(round(100*lower/len(s),2), round(100*(len(s)-lower)/len(s),2))
