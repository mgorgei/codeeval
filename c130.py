import re
def f(s):
    s = s.split()
    rgx = ""
    for digit in s[0]:
        if digit == '0':
            rgx+= "A+"
        else:
            rgx+= "(A+|B+)"
    match = re.match(rgx, s[1])
    if match:
        return "Yes"
    else:
        return "No"

'''
f("1010 AAAAABBBBAAAA")
f("00 AAAAAA")
f("01001110 AAAABAAABBBBBBAAAAAAA")
f("1100110 BBAABABBA")
'''
