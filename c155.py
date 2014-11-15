def f(test='5 | s | 92 112 109 40 118 109 109 108 123 40 119 110 40 124 112 109 40 117 105 118 129 40 119 125 124 127 109 113 111 112 40 124 112 109 40 118 109 109 108 123 40 119 110 40 124 112 109 40 110 109 127 54 40 53 40 91 120 119 107 115\n'):
    duplen, lastchar, message = test.rstrip('\n').split('|')
    duplen = int(duplen)
    lastchar = lastchar[1:-1]
    message = [int(x) for x in message.split()]
    for i in range(len(message) - duplen):
        for j in range(i + duplen, len(message) - duplen):
            rem = 0
            while duplen != rem:
                if (message[i + rem] != message[j + rem] and
                    message[i + rem] != message[j + rem] + 32 and
                    message[i + rem] != message[j + rem] - 32):
                    break
                rem+=1
            if rem == duplen:
                distance = ord(lastchar) - message[i + duplen - 1]
                potential = map(lambda x: chr(x + distance), message[i:i + duplen])
                potential = ''.join(list(potential))
                if potential.isalpha():
                    result = map(lambda x: chr(x + distance), message)
                    print( ''.join(result) )
                    return

    '''for i in range(len(test[2]) - int(test[0])):
        for j in range(i+1, len(test[2]) - int(test[0])):
            if test[2][i:i + int(test[0]) + 1] == test[2][j:j + int(test[0]) + 1]:
                #how to separate spaces (or any punctuation) from message
                #without explicitly looking for most used character
                #and assuming that it is space...
                #also may have to deal with capitalization +/- 32 of first char
                print(test[2][i+ int(test[0]) + 1], i, j)
                break
        else:
            continue
        break
    test[0] = '8'#<-- need to find out 'n' instead of using hard-coded value
    test[2] = [int(x) for x in test[2].split()]
    test[2] = map(lambda x: chr(x - int(test[0])), test[2])
    print(''.join(test[2]))
'''
