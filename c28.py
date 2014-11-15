import re
def f(test):
    string, sub = test.rstrip('\n').split(',')
    escaped = False
    rgx = ''
    for char in sub:
        if char == '\\' and escaped == False:
            escaped = True
            continue#?
        elif escaped:
            escaped = False
            if char == '*':
                rgx+= '\\*'
            else:
                rgx+= char
        elif char == '*' :
            rgx+= '.*'
        else:
            rgx+= char
    '''x = re.search(rgx,string)
    if x:
        print('|',x.group(),'|', rgx)'''
    print('true') if re.search(rgx, string) else print('false')
