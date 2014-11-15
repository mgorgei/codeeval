def f(test='{\"id\": 46, \"label\": \"Label 46\"}'):
    test = test.rstrip().split('"label":')
    total = 0
    for label in test:
        try:
            index = label.rindex('{\"id\": ')
            total+= int( label[index+7: label.rindex(',')] )
        except:
            pass
    print(total)
