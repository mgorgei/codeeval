from collections import deque
def f(test='10,3'):
    test = test.rstrip().split(',')
    people = deque( range(int(test[0])) )
    result = ""
    while len(people):
        people.rotate(-int(test[1])+ 1)
        result += str(people.popleft()) + ' '
    print(result[:-1])
