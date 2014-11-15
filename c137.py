import re
def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

def validate_IPv4(x0,x1,x2,x3):
    for i in range(4):
        if eval('x' + str(i) + '< 0 or x' + str(i) + '> 255'):
            return False
    if x0 == 1 and x1 == 0 and x2 == 0 and x3 == 0:
        return False
    if x0 == 255 and x1 == 255 and x2 == 255 and x3 == 254:
        return False
    return True

def countIP(x, iplist, ipcount):
    if validate_IPv4(x[0],x[1],x[2],x[3]):
        if not x in iplist:
            iplist.append(x)
            ipcount.append(1)
        else:
            ipcount[iplist.index(x)]+= 1

def f (file='t137.txt'):
    file = open(file)
    iplist = [0]
    ipcount = [0]
    for test in file:
        test = test.rstrip()
        #dotted hex
        rgx = "(?:0x[0-9A-Fa-f]{1,2}[.]){3}0x[0-9A-Fa-f]{1,2}"
        search = re.search(rgx, test)
        if search:
            x = search.group().split('.')
            for i in range(4):
                x[i] = int(x[i],16)
            countIP(x, iplist, ipcount)
        #hexadecimal
        rgx = "(?:0x[0-9A-Fa-f]{8})"
        search = re.search(rgx, test)
        if search:
            x = [0,0,0,0]
            for i in range(4):
                x[i] = int(search.group()[i*2 + 2:i*2 + 4], 16)
            countIP(x, iplist, ipcount)
        #dotted octal
        rgx = "(?:[0-7]{4})(?:[.][0-7]{4}){3}"
        search = re.search(rgx, test)
        if search:
            x = search.group().split('.')
            for i in range(4):
                x[i] = int(x[i],8)
            countIP(x, iplist, ipcount)
        #octal
        rgx = "(?:[0-7]{12,16})"
        search = re.search(rgx, test)
        if search:
            x = [0,0,0,0]
            for i in range(4):
                x[i] = int(search.group()[i*3:i*3 + 3], 8)
            countIP(x, iplist, ipcount)
        #dotted binary
        rgx = "(?:[01]){8}(?:[.][01]{8}){3}"
        search = re.search(rgx, test)
        if search:
            x = search.group().split('.')
            for i in range(4):
                x[i] = int(x[i],2)
            countIP(x, iplist, ipcount)
        #binary
        rgx = "(?:[01]){32}"
        search = re.search(rgx, test)
        if search:
            x = [0,0,0,0]
            for i in range(4):
                x[i] = int(search.group()[i*8:i*8 + 8], 2)
            countIP(x, iplist, ipcount)
    zipped = zip(ipcount, iplist)
    zipped = sorted(zipped, key=lambda x:x[0], reverse=True)
    count, lst = zip(*zipped)
    ties = 1
    for i in range(len(count)-1):
        if count[i] == count[i+1]:
            break
        else:
            ties+= 1
    result = ""
    for i in range(ties-1):
        #lst = sorted(lst)!!!!
        flat = ""
        for j in range(4):
            flat+= str(lst[i][j]) + '.'
        result+= flat[:-1] + ' '
    return result.rstrip()
