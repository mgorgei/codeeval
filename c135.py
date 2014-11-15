from itertools import permutations
from copy import deepcopy
class Candidate():
    def __init__(self, head):
        self.head = head
        self.left = []
        self.right = []

    def __len__(self):
        return len(self.left) + len(self.right)

def f(test='soup,sugar,peas,rice'):
    chain = test.rstrip().split(',')
    count = []
    candidates = []
    for i in range(len(chain)):
        c = Candidate(chain[i])
        for j in range(len(chain)):
            if j != i:
                if chain[i][0] == chain[j][-1]:
                    c.left.append(chain[j])
                if chain[i][-1] == chain[j][0]:
                    c.right.append(chain[j])
        candidates.append(c)
    #print( sum(len(c) for c in candidates) )
    
    p = permutations(chain)#brute forced...
    
    for case in p:
        count.append(1)
        for j in range(len(case) - 1):
            if case[j][-1] == case[j+1][0]:
                count[-1] += 1
            else:
                break
    
    #return
    count = max(count)
    if count == 1:
        print(None)
    else:
        print(count)

'''
left self right
uniq = chain

left  self  right
----  ----  ----
peas  soup  peas

peas  sugar rice

sugar rice

soup  peas  sugar
            soup
'''
