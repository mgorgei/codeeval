def f(test='2 100\n'):#14
    #what is the worst case number of tries need to find the floor
    #given that the first few could crack, but also give a good indication of
    #where to subdivide the list of positions
    eggs, floors = test.rstrip('\n').split()
    n = float(floors)
    while n:
        n/= eggs
        print(n)
