'''MORSE CODE

You have received a text encoded with Morse code and want to decode it.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following:
.- ...- ..--- .-- .... .. . -.-. -..-  ....- .....
-... .... ...--
Each letter is separated by space char, each word is separated by 2 space chars.

OUTPUT SAMPLE:
Print out decoded words. E.g.
AV2WHIECX 45
BH3
You program has to support letters and digits only.
'''
def f(test):
    morse = {          
          "0": "-----",      "1": ".----",      "2": "..---",      "3": "...--", 
          "4": "....-",      "5": ".....",      "6": "-....",      "7": "--...", 
          "8": "---..",      "9": "----.", 
          "A": ".-",         "B": "-...",       "C": "-.-.",       "D": "-..", 
          "E": ".",          "F": "..-.",       "G": "--.",        "H": "....", 
          "I": "..",         "J": ".---",       "K": "-.-",        "L": ".-..", 
          "M": "--",         "N": "-.",         "O": "---",        "P": ".--.", 
          "Q": "--.-",       "R": ".-.",        "S": "...",        "T": "-", 
          "U": "..-",        "V": "...-",       "W": ".--",        "X": "-..-", 
          "Y": "-.--",       "Z": "--.."}
    test = test.split('  ')
    result = ""
    for word in test:
        chars = word.split()
        for char in chars:
            result+= [k for k,v in morse.items() if v == char][0]
        result+= ' '
    print(result)
