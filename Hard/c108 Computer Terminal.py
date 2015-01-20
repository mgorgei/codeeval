'''COMPUTER TERMINAL

In this problem you are writing the software for a small terminal with a 10-row,
10-column display (perhaps for a point-of-sale terminal). Rows and columns are
numbered 0 through 9. The character that introduces a control sequence is ^, the
circumflex. The character (or in one case, the two characters) immediately
following the control sequence introducer will direct your software in
performing its special functions.

Here is the complete list of control sequences you will need to interpret: 
^c - clear the entire screen; the cursor row and column do not change 
^h - move the cursor to row 0, column 0; the image on the screen is not changed 
^b - move the cursor to the beginning of the current line; the cursor row does not change 
^d - move the cursor down one row if possible; the cursor column does not change 
^u - move the cursor up one row, if possible; the cursor column does not change 
^l - move the cursor left one column, if possible; the cursor row does not change 
^r - move the cursor right one column, if possible; the cursor row does not change 
^e - erase characters to the right of, and including, the cursor column on the cursor's row; the cursor row and column do not change 
^i - enter insert mode 
^o - enter overwrite mode 
^^ - write a circumflex (^) at the current cursor location, exactly as if it was not a special character; this is subject to the actions of the current mode (insert or overwrite) 
^DD - move the cursor to the row and column specified; each D represents a decimal digit; the first D represents the new row number, and the second D represents the new column number 

No illegal control sequences will ever be sent to the terminal. The cursor
cannot move outside the allowed screen locations (that is, between row 0, column
0 and row 9, column 9). 
When a normal character (not part of a control sequence) arrives at the terminal
, it is displayed on the terminal screen in a manner that depends on the
terminal mode. When the terminal is in overwrite mode (as it is when it is first
turned on), the received character replaces the character at the cursor's
location. But when the terminal is in insert mode, the characters to the right
of and including the cursor's location are shifted right one column, and the new
character is placed at the cursor's location; the character previously in the
rightmost column of the cursor's row is lost. 
Regardless of the mode, the cursor is moved right one column, if possible.

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Input
example is the following

^h^c^04^^^13/ \^d^b  /   \^u^d^d^l^l^l^l^l^l^l^l^l^r^r^l^l^d
<CodeEval >^l^l^d/^b \^d^r^r^66/^b  \^b^d   \ /^d^l^lv^d^b===========^i^
94O123456789^94A=======^u^u^u^u^u^u^l^l\^o^b^r/

OUTPUT SAMPLE:
Print results in the following way.

    ^
   / \
  /   \
 /     \
<CodeEval>
 \     /
  \   /
   \ /
    v
====A=====
'''
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
