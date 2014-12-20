'''DELTA TIME

You are given the pairs of time values. The values are in the HH:MM:SS format
with leading zeros. Your task is to find out the time difference between the
pairs.

INPUT SAMPLE:
The first argument is a file that contains lines with the time pairs.
For example:
14:01:57 12:47:11
13:09:42 22:16:15
08:08:06 08:38:28
23:35:07 02:49:59
14:31:45 14:46:56

OUTPUT SAMPLE:
Print to stdout the time difference for each pair, one per line. You must format
the time values in HH:MM:SS with leading zeros.
For example:
01:14:46
09:06:33
00:30:22
20:45:08
00:15:11
'''
import datetime
def f(test):
    test = test.split()
    a = test[0].split(":")
    b = test[1].split(":")
    t1 = datetime.time(int(a[0]),int(a[1]),int(a[2]))
    t2 = datetime.time(int(b[0]),int(b[1]),int(b[2]))
    if t1 > t2:
        t1, t2 = t2,t1
    dummydate = datetime.datetime(2000,1,1)
    result = datetime.datetime.combine(dummydate,t2) - datetime.datetime.combine(dummydate,t1)
    dummydate = dummydate + result
    print(dummydate.strftime("%H:%M:%S"))
