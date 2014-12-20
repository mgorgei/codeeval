'''Reverse Words

Write a program which reverses the words in an input sentence.

INPUT SAMPLE:
The first argument is a file that contains multiple sentences, one per line.
Empty lines are also possible.

Hello World
Hello CodeEval

OUTPUT SAMPLE:
Print to stdout each sentence with the reversed words in it, one per line.
Empty lines in the input should be ignored. Ensure that there are no trailing
empty spaces in each line you print.

World Hello
CodeEval Hello
'''
def f(test='Hello World'):#World Hello
    test = test.rstrip().split()
    print(' '.join(test[::-1]))
