def f(test='$#**\\0100000101101100011100101000\n'):# ##*\$
    test = test.rstrip('\n')
    index0 = test.find('0')
    index1 = test.find('1')
    index = min(index0, index1)
    string = test[:index]
    binary = test[index:]
    length = 0
    print(string,binary)
    sequence = []
    unique = []
    mapstring = []
    while binary:
        if length == 0:
            #get next three chars
            length = int(binary[:3],2)
            binary = binary[3:]
            if length == 0:
                break#unnecessary?
            continue
        else:
            seq = binary[:length]
            binary = binary[length:]
            if seq == '1'*length:
                length = 0
            else:
                sequence.append(seq)
                '''if not seq in unique:
                    unique.append(seq)'''
    for char in string:
        #if not char in mapstring:
        mapstring.append(char)
    mapping = sorted(sequence, key=lambda x: (len(x),x))
    print(sequence,mapping,mapstring)
    result = []
    for s in sequence:
        result.append(mapstring[mapping.index(s)])
    print(''.join(result))

'''
The first key in the sequence is of length 1, the next 3 are of length 2, the
next 7 of length 3, the next 15 of length 4, etc. If two adjacent keys have the
same length, the second can be obtained from the first by adding 1 (base 2).
Notice that there are no keys in the sequence that consist only of 1's. 

The input file contains several data sets. Each data set consists of a header
and a message. These will all be on one line. The length of the header is
limited only by the fact that key strings have a maximum length of 7 (111 in
binary). If there are multiple copies of a character in a header, then several
keys will map to that character. The encoded message contains only 0's and 1's,
and it is a legitimate encoding according to the described scheme. That is, the
message segments begin with the 3-digit length sequence and end with the
appropriate sequence of 1's. The keys in any given segment are all of the same
length, and they all correspond to characters in the header. The message is
terminated by 000. Your program should accept the first argument as the filename
and read the contents of this file as the test data, according to the conditions
above. E.g.
010 00 00 10 11; 011 000 111; 001 0 1; 000
segment length is 2; terminated by 11
segment length is 3; terminated by 111
segment length is 1; terminated by 1?
$  #   *   * \
00 00 10 000 0   order
0  00  10    000 mapping
0  00 -00-10 000 alt mapping???
##*\$
sorted(x, key=lambda x: (len(x),x))
'''
