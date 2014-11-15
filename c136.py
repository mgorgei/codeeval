def f():
    test_cases = open('t136.txt', 'r')
    start = -1
    direction = ['/', '|', '\\']
    for test in test_cases:
        test = test.strip()
        output = ""
        i = 0
        if start == -1:
            for char in test:
                if char == '_':
                    start = i
                    output = test[:start] + '|' + test[start+1:]
                    break
                i+=1
        else:
            for i in range(-1, 1 + 1):
                if test[start + i] == 'C':
                    output = test[:start+i] +  direction[i + 1] + test[start+i+1:]
                    start+= i
                    break
            else:
                for i in range(-1, 1 + 1):
                    if test[start + i] == '_':
                        output = test[:start+i] +  direction[i + 1] + test[start+i+1:]
                        start+= i
                        break
        print(output)
