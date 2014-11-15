roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def f(test='2I3I2X9V1X'):
    test = test.rstrip()
    result = 0
    for i in range(1, len(test)-2, 2):
        result+= roman[test[i]] * int(test[i-1]) * (-1 if roman[test[i]] < roman[test[i+2]] else 1)
    #if len(test) > 2:
    result+= roman[test[-1]] * int(test[-2])
    print(result)
