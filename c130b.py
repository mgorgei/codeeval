#no upload
def f(test='00111011 AAAAAAAABBBBBBAAAAAAAAA\n'):
    seq, ab = test.rstrip('\n').split()
    matrix = [[None for s in range(len(ab))] for a in range(len(seq))]
    g(seq, ab, matrix)
    print('Yes') if matrix[-1][-1] else print('No')

def g(seq, ab, matrix, row=0, col=0):
    if matrix[-1][-1]: return
    if matrix[row][col]: return
    for c in range(col, len(ab)):
        matrix[row][c] = False
        if match(seq[row], ab[col:c+1]):
            matrix[row][c] = True
            if row+1 < len(matrix) and c+1 < len(matrix[row]): 
                g(seq, ab, matrix, row+1, c+1)

def match(seq, ab):
    if seq == '0':
        return 'B' not in ab
    if seq == '1':
        a = 'A' in ab
        b = 'B' in ab
        return not(a and b)
