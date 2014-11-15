from collections import deque
def f(test='10 -2 3 4'):
    test = test.rstrip().split()
    stack = deque(test)
    result = ""
    for i in range( (len(stack)+ 1)//2 ):
        result+= stack.pop() + ' '
        stack.rotate(1)
    print(result[:-1])
