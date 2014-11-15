import re
def f(test='*7* johab.py gen_probe.ko palmtx.h macpath.py tzp dm-dirty-log.h bh1770.h pktloc faillog.8.gz zconf.gperf'):
    test = test.rstrip('\n').split()
    rgx = '^'
    for char in test[0]:
        if char == '*':
            rgx+= '.*'
        elif char == '?':
            rgx+= '.'
        elif char == '.':
            rgx+= '[.]'
        else:
            rgx+= char
    rgx+='$'
    out = []
    for i in range(1, len(test)):
        result = re.match(rgx, test[i])
        if result:
            out.append(result.group())
    if out:
        print(' '.join(out))
    else:
        print('-')
