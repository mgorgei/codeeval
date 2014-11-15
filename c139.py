import calendar
import datetime

def g(date):#onverts it into the distance of months from Jan 1990
    date = date.split()
    return list(calendar.month_abbr).index(date[0]) + (int(date[1]) - 1990) * 12

def f(test='Feb 2004-Dec 2009; Sep 2004-Jul 2008'):
    months = [0] * 372#The dates are in range [Jan 1990, Dec 2020] (31 years)
    test = test.split(';')
    for i in test:
        i = i.split('-')
        for j in range(g(i[0]), g(i[1]) +1):
            months[j] = 1
    #print(months)
    print(sum(months) // 12)

