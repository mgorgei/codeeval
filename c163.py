def f(test='1'):#   0123456789
    charmap = []
    charmap.append('-**----*--***--***---*---****--**--****--**---**--')
    charmap.append('*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-')
    charmap.append('*--*---*---**---**--****-***--***----*---**---***-')
    charmap.append('*--*---*--*-------*----*----*-*--*--*---*--*----*-')
    charmap.append('-**---***-****-***-----*-***---**---*----**---**--')
    charmap.append('--------------------------------------------------')
    test = test.strip()
    bnum = []
    for digit in test:
        if digit.isnumeric():
            bnum.append(digit)
    sol = []
    sol.append("")
    sol.append("")
    sol.append("")
    sol.append("")
    sol.append("")
    sol.append("")
    for i in range(6):
        for num in bnum:
            x = 'sol[' + str(i) + ']+=' + 'charmap[' + str(i) + '][' + str(int(num)*5) + ':' + str((int(num)+1)*5) + ']'
            exec(x)
    result = ""
    for i in range(6):
        result += eval('sol[' + str(i) + ']') + ' \n'
    print(result[:-1])
