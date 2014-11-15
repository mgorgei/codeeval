from copy import deepcopy
def f(test='14; 1:[2, 7, 5, 13, 1, 11], 2:[12, 1, 4, 6, 9], 3:[4, 5, 13, 8], 4:[4, 13, 9, 10, 14, 2, 5, 3], 5:[6, 2, 8, 5, 14, 13, 11], 6:[7, 3, 8, 6, 10, 12, 9], 7:[1, 3, 12, 11, 8, 2, 7], 8:[4, 10, 3, 9, 5, 11], 9:[9, 14, 10, 12, 1, 4, 8], 10:[1, 8, 12, 9, 14, 10], 11:[13], 12:[9, 5, 11, 14, 3, 6, 1, 4], 13:[9, 10, 4, 12, 2, 11], 14:[10, 9]'):#'4; 1:[1, 3, 2], 2:[1], 3:[4, 3], 4:[4, 3]\n'):
    number, team = test.rstrip(']\n').split(';')
    number = int(number)
    team = team.split('],')
    unique = []
    for i in range(len(team)):
        team[i] = team[i][team[i].find(':[')+2:]
        team[i] = team[i].split(', ')
        for seat in team[i]:
            if not seat in unique:
                unique.append(seat)
    #remove individual entries from unique and team!
    '''i = 0
    while i < len(team):
        popped = False
        #print(team[i])
        if len(team[i]) == 1 and team[i][0] in unique:
            unique.remove(team[i][0])
            #remove entry from each member in team...
            for j in range(len(team)):
                if team[i][0] in team[j] and i != j:
                    team[j].remove(team[i][0])
            team.pop(i)
            popped = True
        if not popped:
            i+= 1
    for t in team:
        print(t)'''
    if number == len(unique) and g(team,unique):
        print('Yes')
    else:
        print('No')

def g(desired_positions, open_positions):
    if not open_positions:
        return True
    for path in desired_positions[0]:
        if path in open_positions:
            temp = deepcopy(open_positions)
            temp.remove(path)
            if g(desired_positions[1:], temp):
                return True
    return False
