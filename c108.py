row = 0#0-9
col = 0#0-9
terminal = [' '*10]*10#[row][col]
overwrite = True#False = insert mode
def f(test):
    test = test.rstrip('\n')
    global row
    global col
    global terminal
    global overwrite
    circumflex = False
    for char in test:
        if char == '^' and circumflex == False:
            circumflex = True
            continue
        if circumflex:
            if char.isdigit():
                if circumflex == 1:
                    row = int(char)
                    circumflex = 2
                else:
                    col = int(char)
                    circumflex = False
            elif char == 'h':
                row = 0
                col = 0
            elif char == 'u':
                if row > 0:
                    row-=1
            elif char == 'd':
                if row < 9:
                    row+=1
            elif char == 'l':
                if col > 0:
                    col-=1
            elif char == 'r':
                if col < 9:
                    col+=1
            elif char == 'b':
                col = 0
            elif char == '^':
                write_char(char)
                '''^e - erase characters to the right of, and including,
the cursor column on the cursor's row; the cursor row and column do not change'''
            elif char == 'e':
                terminal[row] = terminal[row][:col] + ' ' * (10 - col)
            elif char == 'c':
                terminal = [' '*10]*10
            elif char == 'i':
                overwrite = False
            elif char == 'o':
                overwrite = True
            if circumflex < 2:
                circumflex = False
        else:
            write_char(char)
    print(row, col)
    for line in terminal:
        print(line)
def write_char(char):
    global row
    global col
    global terminal
    global overwrite
    if overwrite:
        terminal[row] = terminal[row][:col] + char + terminal[row][col+1:]
    else:
        terminal[row] = terminal[row][:col] + char + terminal[row][col:-1]
    if col < 9:
        col+= 1
'''
When the terminal is in overwrite mode, the received character replaces the
character at the cursor's location.

But when the terminal is in insert mode, the characters to the right
of and including the cursor's location are shifted right one column, and the
new character is placed at the cursor's location; the character previously in
the rightmost column of the cursor's row is lost.

Regardless of the mode, the cursor is moved right one column, if possible.
'''
