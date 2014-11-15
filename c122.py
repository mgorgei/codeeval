def f(test):
    test = test.translate(str.maketrans(
        "abcdefghij",
        "0123456789",
        ))
    result = ""
    for i in test:
        if i.isdigit():
            result+=i
    if result:
        print(result)
    else:
        print("NONE")
