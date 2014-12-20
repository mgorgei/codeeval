'''MIXED CONTENT

You have a string of words and digits divided by comma. Write a program which
separates words with digits. You shouldn't change the order elements.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following

8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
24,13,14,43,41

OUTPUT SAMPLE:
melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
24,13,14,43,41
As you cas see you need to output the same input string if it has words only or
digits only.
'''
def f(test='8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21'):
    test = test.rstrip().split(',')
    strings, numbers = [], []
    for content in test:
        if content.isnumeric():
            numbers.append(content)
        else:
            strings.append(content)
    print(','.join(strings) + (strings != []) * '|' + ','.join(numbers))
