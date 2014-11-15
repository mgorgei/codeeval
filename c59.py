#permutation combination
keys = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
def f(test='4155230'):
    numbers = []
    g('', test, numbers)
    print(','.join(numbers))

def g(combo,test,numbers):
    if test == '':
        numbers.append(combo)
    else:
        for key in keys[int(test[0])]:
            g(combo + key, test[1:], numbers)
'''
0 => 0
1 => 1
2 => abc
3 => def
4 => ghi
5 => jkl
6 => mno
7 => pqrs
8 => tuv
9 => wxyz
'''
