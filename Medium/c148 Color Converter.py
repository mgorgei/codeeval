'''COLOR CODE CONVERTER

Your challenge is to write a program to convert different types of color codes.
You will need to be able to convert color codes between CMYK, Hex, HSL, HSV and
RGB. The converter should accept codes formatted as follows:

HSL: "HSL(D,P,P)"
HSV: "HSV(D,P,P)"
CMYK: "(F,F,F,F)"
Hex: "#000000"
Where: 'D' is in range [0, 359] degrees, 'P' is in range [0, 100] percent, 'F'
is a float, rounded to a second digit after dot in range [0.00, 1.00], Hex is
in range [#000000, #ffffff]

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
of the file contains a color in one of a described codes. E.g.

(0.56,0.94,0.21,0.02)
HSL(359,0,0)
HSV(276,33,7)
#cfa9c4

OUTPUT SAMPLE:
For each line of input determine the color code, convert it to RGB and print out
the result, rounding a float numbers to a nearest whole integer. E.g.

RGB(110,15,197)
RGB(0,0,0)
RGB(15,12,18)
RGB(207,169,196)
'''
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
