def f(test='2 5'):
    a, n = test.rstrip('\n').split(' ')
    a = int(a) - 2
    n = int(n)
    digits = [0,0,0,0,0,0,0,0,0,0]
    pattern = [[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
    copies = n // len(pattern[a])
    for i in range(len(pattern[a])):
        digits[pattern[a][i]] = copies
    remainder = n % len(pattern[a]) 
    for i in range(remainder):
        digits[pattern[a][i]] += 1
    result = ''
    for i in range(10):
        result+= str(i) + ': {}, '.format(digits[i])
    print(result[:-2])
