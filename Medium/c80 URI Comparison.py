'''URI COMPARISON

Determine if two URIs match. For the purpose of this challenge, you should use a
case-sensitive octet-by-octet comparison of the entire URIs, with these
exceptions: 

1. A port that is empty or not given is equivalent to the default port of 80 
2. Comparisons of host names MUST be case-insensitive 
3. Comparisons of scheme names MUST be case-insensitive 
4. Characters are equivalent to their % HEX HEX encodings. (Other than typical
reserved characters in urls like , / ? : @ & = + $ #)

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains two urls delimited by a semicolon. E.g.

http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html

OUTPUT SAMPLE:
Print out True/False if the URIs match. E.g.

True
'''
def f(test='http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html'):
    test = test.rstrip().split(';')
    for i in [0,1]:
        test[i] = test[i].lower()
        while test[i].find('%') != -1:
            index = test[i].index('%')
            try:
                char = chr(int(test[i][index+1:index+3],16))
                test[i] = test[i][:index] + char + test[i][index+3:]
            except:
                char = '!'
                test[i] = test[i][:index] + char + test[i][index+1:]
        index = test[i].find('://')
        pindex = test[i][index+3:].find(':')
        if pindex == -1:
            pindex = test[i][index+3:].find('/')
            test[i] = test[i][:index+pindex+3] + ':80' + test[i][index+pindex+3:]
            #print(index, pindex)
    #print(test[0], test[1])
    print(test[0] == test[1])
