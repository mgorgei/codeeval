def isPrime2(number):  
    if number <= 1:
        return False
    for check in range(2, number):
        if (number%check) == 0:
            return False
    return True

def is_palindrome_v3(s):     
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i-1]:
            return False
    return True

def f():
    for i in range(1001, 0,-1):
        if is_palindrome_v3(str(i)):
            if isPrime2(i):
                print(i)
                return
