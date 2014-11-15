from collections import deque
def f(test='3;3;1 2 3 4 5 6 7 8 9'):
    stop, right, down, left, up = range(5)
    direction  = deque(range(1,5))
    test = test.rstrip().split(';')
    vbound = int(test[0])
    hbound = int(test[1])
    test[2] = test[2].split()
    traveled = []
    for col in range(vbound):
        slist = []
        for row in range(hbound):
            slist.append(test[2][row + col*hbound])
        traveled.append(slist)
    result = ''
    h = 0
    v = 0
    hiccup = False
    while True:
        if traveled[v][h] == None:
            if hiccup:
                break
            else:
                hiccup = True
                h+= -1*(direction[0] < 3) +1*(direction[0] > 2)
                v+= -1*(direction[1] > 2) +1*(direction[1] < 3)
                direction.rotate(-1)
                continue
        hiccup = False
        result+= traveled[v][h] + ' '
        traveled[v][h] = None
        #right
        if direction[0] == right:
            if h + 1 >= hbound:
                direction.rotate(-1)
                v+=1
            else:
                h+= 1
        #down
        elif direction[0] == down:
            if v + 1 >= vbound:
                direction.rotate(-1)
                h-=1
            else:
                v+= 1
        #left
        elif direction[0] == left:
            if h - 1 < 0:
                direction.rotate(-1)
                v-=1
            else:
                h-= 1
        #up
        elif direction[0] == up:
            if v - 1 < 0:
                direction.rotate(-1)
                h+=1
            else:
                v-= 1
    print(result)
