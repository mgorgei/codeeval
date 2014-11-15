def f(test='6'):
    size = int(test.rstrip())
    triangle = []
    for n in range(1, size+1):
        triangle.append([1 if i==0 or i==n-1 else 0 for i in range(n)])
    result = ""
    for depth in range(size):
        for index in range(len(triangle[depth])):
            if triangle[depth][index] == 0:
                triangle[depth][index] = triangle[depth-1][index-1] + triangle[depth-1][index]
            result+= str(triangle[depth][index]) + ' '
    return result[:-1]
