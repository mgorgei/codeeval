'''THE MINISTRY OF TRUTH

It's 1984, and you are working as an official at the Ministry of Truth. You have
intersected a message subjected to Big Brother's doctrine.

Your task is to delete letters from certain "utterances" in order to replace
them with an "utterance" approved by the Ministry.

A "word" is a single sequence of Latin letters, and an "utterance" is a sequence
of multiple words and spaces.

To compare two "utterances," you have to replace all blocks of spaces with one
space. Utterances are considered to be identical when resulting expressions
match.

One line contains two different expressions separated by semicolon ';'. The
first expression is the original utterance, and the second one is the utterance
you want to get.

If you cannot fulfill the order, print a single line «I cannot fix history».
Otherwise, output the original utterance by replacing the letters that must be
erased with underscore and by replacing all blocks of white spaces with a single
white space.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. E.g.:

Higher meaning;Hi mean
this is impossible;im possible
twenty   two minutes;two minutes
Higher meaning;e

OUTPUT SAMPLE:
Print the results, or "I cannot fix history" in case there is no match. E.g.:

Hi____ mean___
I cannot fix history
______ two minutes
____e_ _______
'''
def f(test='Higher meaning;Hi mean'):
    test = test.rstrip('\n').split(';')
    utterance = test[0].split()
    utter = test[1].split()
    pair = []
    j = 0
    while utterance:
        if utter and utterance[0].find(utter[j]) != -1:
            pair.append( (utterance[0], utter[j]) )
            utterance.pop(0)
            utter.pop(j)
            j = 0
        else:
            if j + 1 < len(utter):
                j+=1
            else:
                pair.append( (utterance[0], '') )
                utterance.pop(0)
                j = 0
        '''if not utter:
            break'''
    if len(utter):
        print("I cannot fix history")
    else:
        result = ''
        for pr in pair:
            index = pr[0].find(pr[1])
            if index != -1:
                under = '_' * (len(pr[0]) - len(pr[1]))
                result += (under[:index] + pr[1] + under[index:]) + ' '
        print(result[:-1])
