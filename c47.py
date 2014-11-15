def is_palindrome(s):     
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i-1]:
            return False
    return True
palindromes = []
truefalse = []
    
#find and record all palindromes in range L R; if count in L1;R1 is even ++
def f(test='1 7'):
    global palindromes
    global truefalse
    interesting = 0
    L, R = test.rstrip('\n').split()
    for i in range(int(L), int(R)+1):
        for j in range(i, int(R)+1):
            count = 0
            for number in range(i, j+1):
                if number in palindromes:
                    if truefalse[palindromes.index(number)]:
                        count+=1
                else:
                    palindromes.append(number)
                    truefalse.append(is_palindrome(str(number)))
                    if truefalse[palindromes.index(number)]:
                        count+=1
            if count % 2 == 0:
                interesting+=1
    print(interesting)
'''ranges:
1 7
1 6
1 5
1 4
1 3
1 2
1 1
2 7
2 6
2 5
2 4
2 3
2 2
3 7
3 6
3 5
3 4
3 3
4 7
4 6
4 5
4 4
5 7
5 6
5 5
6 7
6 6
7 7
'''
