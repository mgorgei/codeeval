'''LETTERCASE PERCENTAGE RATIO

Your goal is to find the percentage ratio of lowercase and uppercase letters in
line below.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
of input contains a string with uppercase and lowercase letters E.g.:
thisTHIS
AAbbCCDDEE
N
UkJ

OUTPUT SAMPLE:
For each line from input, print the percentage ratio of uppercase and lowercase
letters rounded to the second digit after the dot. E.g.:
lowercase: 50.00 uppercase: 50.00
lowercase: 20.00 uppercase: 80.00
lowercase: 0.00 uppercase: 100.00
lowercase: 33.33 uppercase: 66.67
'''
def f(s):
    s = s.strip()
    lower = sum(char.islower() for char in s)
    return "lowercase: {:0.2f} uppercase: {:1.2f}".format(
        round(100*lower/len(s),2), round(100*(len(s)-lower)/len(s),2))
