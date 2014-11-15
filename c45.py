def is_palindrome(s):     
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i-1]:
            return False
    return True

def f(test='195\n'):
    number = test.rstrip()#'195'
    for i in range(100):
        reverse = number[::-1]
        nsum = int(number) + int(reverse)
        if is_palindrome(str(nsum)):
            return "{} {}".format(str(i+1), str(nsum))
        number = str(nsum)
    return "fail"
