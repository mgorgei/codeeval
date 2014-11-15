from math import sqrt
def f(test='10'):
    n = int(test)
    count = 0
    stop = int(sqrt(n / 2.0)) +1 
    for i in range(stop):
        if sqrt(n-i*i).is_integer():
            print(n-i*i, i*i, i)
            count+=1
    print('number:', n)
    return count

print (f(20) == 1,f(25) == 2,f(17) == 1,f(13) == 1,
       f(10) == 1,f(8) == 1,f(5) == 1,f(2) == 1,
       f(1) == 1,f(0) == 1,f(48612265) == 32, f(50) == 2)
