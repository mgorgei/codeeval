'''SLANG FLAVOR

Long serious texts are boring. Write a program that will make texts more
informal: replace every other end punctuation mark (period '.', exclamation mark
'!', or question mark '?') with one of the following slang phrases, selecting
them one after another:

', yeah!'
', this is crazy, I tell ya.'
', can U believe this?'
', eh?'
', aw yea.'
', yo.'
'? No way!'
'. Awesome!'
The result should be funny.

INPUT SAMPLE:
The first argument is a file that contains a text.

For example:

Lorem ipsum dolor sit amet. Mea et habeo doming praesent. Te inani utroque recteque has, sea ne fugit verterem!
Usu ei scripta phaedrum, an sed salutatus definiebas? Qui ut recteque gloriatur reformidans. Qui solum aeque sapientem cu.
Eu nam nusquam quaestio principes.

OUTPUT SAMPLE:
Print to stdout the results: the text with slang phrases.

For example:

Lorem ipsum dolor sit amet. Mea et habeo doming praesent, yeah! Te inani utroque recteque has, sea ne fugit verterem!
Usu ei scripta phaedrum, an sed salutatus definiebas, this is crazy, I tell ya. Qui ut recteque gloriatur reformidans. Qui solum aeque sapientem cu, can U believe this?
Eu nam nusquam quaestio principes.
'''
phrases = [', yeah!',
', this is crazy, I tell ya.',
', can U believe this?',
', eh?',
', aw yea.',
', yo.',
'? No way!',
'. Awesome!']

def f(test='''Lorem ipsum dolor sit amet. Mea et habeo doming praesent. Te inani utroque recteque has, sea ne fugit verterem!
Usu ei scripta phaedrum, an sed salutatus definiebas? Qui ut recteque gloriatur reformidans. Qui solum aeque sapientem cu.
Eu nam nusquam quaestio principes.'''):
    test = test.rstrip()
    punctuation_count = 0
    result = ""
    for char in test:
        if char == '.' or char == '!' or char == '?':
            punctuation_count+=1
            if punctuation_count % 2 == 0:
                result+= phrases[(punctuation_count // 2 - 1) % len(phrases)]
            else:
                result+= char
        else:
            result+= char
    print(result)
