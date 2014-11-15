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
