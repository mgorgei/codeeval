'''BATS CHALLENGE

Outside of your window, there's a wire between two buildings. Bats love to hang
there but you notice they never hang closer than "d" centimeters from each
other. They also don't hang closer than 6 centimeters from any of the buildings.

Your goal is to determine the maximum number of additional bats that can fit on
that wire assuming they have zero width.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename.
Each line of input contains three space separated integers: the length of the
wire "l", distance "d" and number of bats "n" already hanging on the wire.

"n" numbers contain the positions of the bats in any order. All number are
integers. You can assume that the bats already hanging on the wire are at least
6 cm from the poles and at least "d" centimeters apart from each other.:

22 2 2 9 11
33 5 0
16 3 2 6 10
835 125 1 113
47 5 0

OUTPUT SAMPLE:
For each line of input print out one integer to determine the maximum number of
additional bats that can possibly hang on he wire. E.g:

3
5
0
5
8
'''
def f(test='22 2 2 9 11', pole=6):
    test = test.rstrip().split()
    length = int(test[0])
    distance = int(test[1])
    n = int(test[2])
    bats = [int(x) for x in test[3:]] if n else []
    bats = sorted(bats)
    left = pole
    right = length - pole
    if bats:
        if left < bats[0] - distance:
            bats.insert(0,left)
    else:
        bats.insert(0,left)
    index = 0
    bound = 0
    while True:
        if index + 1 < len(bats):
            bound = bats[index+1]
        else:
            bound = right
        if bats[index] + distance <= bound - distance:
            bats.append(bats[index] + distance)
            bats.sort()
        index+=1
        if index >= len(bats):
            break
    while bats[-1] + distance <= right:
        bats.append(bats[-1] + distance)
    return len(bats) - n
