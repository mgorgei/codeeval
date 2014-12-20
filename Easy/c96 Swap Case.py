'''SWAP CASE

Write a program which swaps letters' case in a sentence. All non-letter
characters should remain the same.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following

Hello world!
JavaScript language 1.8
A letter

OUTPUT SAMPLE:
Print results in the following way.

hELLO WORLD!
jAVAsCRIPT LANGUAGE 1.8
a LETTER
'''
def f(test='Hello world!'):
    test = test.rstrip()
    result = ""
    for char in test:
        if char.isalpha():
            if char.islower():
                result+= char.upper()
            else:
                result+= char.lower()
        else:
            result+= char
    print(result)
