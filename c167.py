def f(test='Two thousand verses is a great many - very, very great many.\n'):
    test_cases = open("t167.txt")
    for test in test_cases:
        test = test.rstrip()
        if len(test) <= 55:
            print(test)
        else:
            trim = test[0:40]
            index = trim.rfind(' ')
            if index != -1:
                print(trim[0:index] + '... <Read More>')
            else:
                print(trim + '... <Read More>')            
'''
Two thousand verses is a great many - ve
Tom exhibited.
Tom exhibited.
Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look.
Amy Lawrence was proud and glad, and she... <Read More>
Tom was tugging at a button-hole and looking sheepish.
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many - very, very great many.
Two thousand verses is a great many -... <Read More>
Tom's mouth watered for the apple, but he stuck to his work.
Tom's mouth watered for the apple, but... <Read More>
123456789A 23456 89B123456789C123456789D123456789E123456789F123456789G
'''
