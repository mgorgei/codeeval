def f(test='2 0 6 3 1 6 3 1 6 3 1'):#len = 11
    test = test.rstrip().split()
    currsequence = ""
    prevsequence = ""
    #start with size of string; index of test string; position to test
    for size in range(1, len(test) // 2 + 1):
        for index in range(len(test) - size + 1):
            position = 0
            while position < len(test) - size:
                if index != position:
                    pass
                print(size, index, position)
                position+= 1
            
                #currsequence = test[:]
                #prevsequence = test[:]
