from copy import deepcopy
sol = []
def f(test='(2,5), 12'):
    global sol
    sol.clear()
    capacity, oil = test.rstrip('\n').split(', ')
    capacity = sorted([int(x) for x in capacity[1:-1].split(',')])
    oil = int(oil)
    g(capacity, oil, [0]*len(capacity))
    if sol:
        sol = sorted(sol)
        for i in range(len(sol)):
            sol[i] = str(sol[i]).replace(' ','')
        print(''.join(sol))
    else:
        print(False)
        '''oil // capacity[0]
        oil % capacity[0]
        #needs to find minimum amount of extra oil needed to fill '''

def g(capacity, oil, tankers):#closest value of oil to any capacity for else...
    global sol
    #print(capacity, oil, tankers)#lowest value of oil could solve the else situation
    if oil == 0:
        if not tankers in sol:
            sol.append(tankers)
        return
    if capacity[0] > oil:
        return
    for i in range(len(capacity)):
        if capacity[i] <= oil:
            temp = deepcopy(tankers)
            temp[i]+= 1
            g(capacity, oil - capacity[i], temp)
    return
    
'''
(2,5), 12
(6,9,20), 44
(197,8170), 155862
(2,4,8), 8
------------------------------
[1,2][6,0]
[1,2,1][4,0,1]
3
[0,0,1][0,2,0][2,1,0][4,0,0]
'''
