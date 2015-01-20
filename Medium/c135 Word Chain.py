'''WORD CHAIN

In this challenge we suggest you to play in the known game "Word chain" in which
players come up with words that begin with the letter that the previous word
ended with. The challenge is to determine the maximum length of a chain that can
be created from a list of words.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains a list of words separated by comma. E.g.

soup,sugar,peas,rice
ljhqi,nrtxgiu,jdtphez,wosqm
cjz,tojiv,sgxf,awonm,fcv

OUTPUT SAMPLE:
Print out the length of the longest chain, print out "None" if there is no
chain. E.g.

4
None
2
'''
def f(test='s1s,s2s,s3s,s4s'):
    chain = test.rstrip().split(',')
    high = 0
    for i in range(len(chain)):
        temp = g([chain[i]], chain[:i] + chain[i+1:])
        if temp > high:
            high = temp
    if high > 1:
        print(high)
    else:
        print('None')

def g(link, chain):
    if chain == "":
        return len(link)
    highest = 0
    for i in range(len(chain)):
        if link[-1][-1] == chain[i][0]:
            stink = link[:]
            stink.append( chain[i] )
            temp = g(stink[:], chain[:i] + chain[i+1:])
            if temp > highest:
                highest = temp
    return max(len(link),highest)
