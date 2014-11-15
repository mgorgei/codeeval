'''
1. A port that is empty or not given is equivalent to the default port of 80 
2. Comparisons of host names MUST be case-insensitive 
3. Comparisons of scheme names MUST be case-insensitive 
4. Characters are equivalent to their % HEX HEX encodings. (Other than typical
reserved characters in urls like , / ? : @ & = + $ #)

INPUT SAMPLE:
http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html
OUTPUT SAMPLE:
True
'''
def f(test='http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html'):
    test = test.rstrip().split(';')
    #ignore case
    #construct regex from first string to match second
    #each character besides '/' may be hex or the original character
    rgx= r'^http://.+[.].+*(:80)?.*$'
