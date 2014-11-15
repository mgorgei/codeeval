def f(test='''message: "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
keyed_alphabet: "BHISOECRTMGWYVALUZDNFJKPQX"'''):
    m, k = test.rstrip('\n').split(',')
    message = m[m.find('\"') + 1:m.rfind('\"')]
    message = message.replace(' ', '  ')#make string homogenous
    keyed_alphabet = k[k.find('\"') + 1:k.rfind('\"')]
    alpha_message = ''
    for i in range(0, len(message), 2):
        #print(message[i:i+2])
        char = ' '
        if message[i] != ' ':
            char = chr(int(message[i:i+2].lstrip('0')) + 64)
            #print(char)
        alpha_message+= char
    #print(alpha_message, message, keyed_alphabet)
    result = alpha_message.translate(str.maketrans(
        keyed_alphabet,
        'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        
        ))
    print(result)
'''
012222 1114142503 0313012513 03141418192102 0113 24191821
BHISOECRTMGWYVALUZDNFJKPQX
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
'ZYXWVUTSRQPONMLKJIHGFEDCBA'
'''
    
'''
alpha, key
BJJ GVVQI IYBQY IVVZDFH BY PDZFDHUY EYUACBD
XOO LYYHP PVXHV PYYTREQ XV IRTERQMV FVMWNXR
key, alpha
ONN WTTMG GJOMJ GTTHDQA OJ ZDHQDAYJ UJYEKOD
LMM DGGNT TQLNQ TGGSWJZ LQ AWSJWZBQ FQBVPLW
'''
