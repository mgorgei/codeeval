'''DECRYPTION

For this challenge you are given an encrypted message and a key. You have to
determine the encryption and encoding technique and then print out the
corresponding plaintext message. You can assume that the plaintext corresponding
to this message, and all messages you must handle, will be comprised of only the
characters A-Z and spaces; no digits or punctuation.

INPUT SAMPLE:
There is no input for this program. The encrypted message and key is:

message: "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
keyed_alphabet: "BHISOECRTMGWYVALUZDNFJKPQX"

OUTPUT SAMPLE:
Print out the plaintext message. (in CAPS)
'''
def f(test='''message: "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119",
keyed_alphabet: "BHISOECRTMGWYVALUZDNFJKPQX"'''):
    m, k = test.rstrip('\n').split(',')
    message = m[m.find('\"') + 1:m.rfind('\"')]
    message = message.replace(' ', '  ')#make string homogenous
    keyed_alphabet = k[k.find('\"') + 1:k.rfind('\"')]
    alpha_message = ''
    for i in range(0, len(message), 2):
        char = ' '
        if message[i] != ' ':
            char = chr(65 + keyed_alphabet.index(chr(65 + int(message[i:i+2].lstrip('0')))))
        alpha_message+= char
    print(alpha_message)
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
