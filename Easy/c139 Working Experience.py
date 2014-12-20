'''WORKING EXPERIENCE

You're building a new social platform and you want to store user's working
experience. You've decided to calculate the total experience in years for each
user based on the time periods entered by users. Using this approach you need to
be sure that you're taking into account overlapping time periods in order to
retrieve an actual working experience in years. E.g. 
Jan 2010-Dec 2010 
Jan 2010-Dec 2010 
Two jobs with 12 months of experience each, but the actual work experience is
1 year, because of overlapping time periods. The challenge is to calculate the
actual working experience based on the list of time intervals.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
of the file contains a list of time periods separated by a semicolon with and a
single whitespace. Each period is represented by begin date and end date. Each
date consists of a month as an abbreviated name and a year with century as a
decimal number separated by a single white space. The begin and end dates are
separated by dash ("-"). E.g.
Feb 2004-Dec 2009; Sep 2004-Jul 2008
Aug 2013-Mar 2014; Apr 2013-Aug 2013; Jun 2014-Aug 2015; Apr 2003-Nov 2004; Apr 2014-Jan 2015
Mar 2003-Jul 2003; Nov 2003-Jan 2004; Apr 1999-Nov 1999
Apr 1992-Dec 1993; Feb 1996-Sep 1997; Jan 2002-Jun 2002; Sep 2003-Apr 2004; Feb 2010-Nov 2011
Feb 2004-May 2004; Jun 2004-Jul 2004

OUTPUT SAMPLE:
For each test case print out the actual work experience in a full years. E.g.
5
4
1
6
0
'''
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
    print(sum(months) // 12)

