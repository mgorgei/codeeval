def f(test=''):
    r=0
    g=0
    b=0
    test = test.rstrip()
    if test.find('#') != -1:
        r = int(test[1:3], 16)
        g = int(test[3:5], 16)
        b = int(test[5:7], 16)
    elif test[0:3] == 'HSL' or test[0:3] == 'HSV':
        HSL = test[2] == 'L'
        test = test[test.index('(')+1:-1]
        test = test.split(',')
        S = float(test[1]) / 100
        LV = float(test[2]) / 100
        if HSL:
            C = (1 - abs(2*LV - 1)) * S
            m = LV - C/2
        else:
            C = LV * S
            m = LV - C
        H = float(test[0]) / 60.0
        X = C*(1 - abs(H % 2 -1) )
        if H < 1:
            r = m + C
            g = m + X
            b = m
        elif H < 2:
            r = m + X
            g = m + C
            b = m
        elif H < 3:
            r = m
            g = m + C
            b = m + X
        elif H < 4:
            r = m
            g = m + X
            b = m + C
        elif H < 5:
            r = m + X
            g = m
            b = m + C
        elif H < 6:
            r = m + C
            g = m
            b = m + X
        r*=255
        g*=255
        b*=255
    elif True:
        test = test[1:-1]
        test = test.split(',')
        r = 255 * (1 - float(test[0])) * (1 - float(test[3]))
        g = 255 * (1 - float(test[1])) * (1 - float(test[3]))
        b = 255 * (1 - float(test[2])) * (1 - float(test[3]))
    print('RGB({:.0f},{:.0f},{:.0f})'.format(r, g, b))
