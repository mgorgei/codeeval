valid=['1','2','3','4','5','6','7','8','9','10','11','12','13','14',
       '15','16','17','18','19','20','21','22','23','24','25','26']
def f(test='1319'):#1 3 1 9,13 1 9, 13 19, 1 3 19; 4
    string = test.rstrip('\n')
    candidates = []
    g(string, '', candidates)
    print((candidates))#len of

def g(original, out, candidates):
    if not original:
        candidates.append(out.lstrip(' '))
        return
    if original[:1] in valid:
        g(original[1:], out + ' ' + original[:1], candidates)
    if len(original) > 1 and original[:2] in valid:
        g(original[2:], out + ' ' + original[:2], candidates)
    

#for every pair, they can exist as:
'''
    n_m
    nm
1227
1 2 2 7
12 2 7
1 22 7
string out
227 1 ;27 12
'''
