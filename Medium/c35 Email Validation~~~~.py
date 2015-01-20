'''EMAIL VALIDATION

You are given several strings that may/may not be valid emails. You should write
a regular expression that determines if the email id is a valid email id or not.
You may assume all characters are from the english language.

INPUT SAMPLE:
Your program should accept as its first argument a filename. This file will
contain several text strings, one per line. Ignore all empty lines. E.g. 

foo@bar.com
this is not an email id
admin#codeeval.com
good123@bad.com

OUTPUT SAMPLE:
Print out 'true' (all lowercase) if the string is a valid email. Else print out
'false' (all lowercase). E.g.

true
false
false
true
'''
import re
def f(test='"very.unusual .@.unusual.com"@example.com'):
    test = test.rstrip()
    comment = "[ \"(),:;<>@[\]\\w.!#$%&'*+-/=?^`{|}~]{1,63}"
    email = "[\w.!#$%&'*+-/=?^`{|}~]{1,63}"
    local = "(?P<comment>[\"])?(?(comment)" + comment + "|" + email + ")(?(comment)[\"])"
    optional = "([\w\-]{1,62}[.])?"
    hostname = "(?<!-)[\w-]{1,63}(?!-)"
    toplevel = "([.][\w\-]{1,62})?"
    domain = optional + hostname + toplevel
    rgx = '^' + local + '@' + domain + '$'
    search = re.match(rgx, test)
    if search:
        print("true")
    else:
        print("false")

'''local part
!#$%&'*+-/=?^_`{|}~ are allowed 0-9a-zA-Z
s[0] != '.' and s[-1]!= '.' '.' cannot be sequential [.]{2}
quotes are permissable from beginning to end or bound by dot seperators ---."---".--- "---"@
 "(),:;<>@[\] are permissable inside quotes, " and \ must be escaped by \
'''
'''domain part
can be IP address if surrounded by square brackets [IP]
***hostname
0-9a-zA-Z-
s[0] != - and s[-1] != - digits maybe are not allowed
underscore is allowed outside hostname


(?<!...)
Matches if the current position in the string is not preceded by a match
for .... This is called a negative lookbehind assertion. Similar to positive
lookbehind assertions, the contained pattern must only match strings of some
fixed length. Patterns which start with negative lookbehind assertions may
match at the beginning of the string being searched.
'''






#p = (<)?     (\w+@\w+(?:\.\w+)+)     (?(1)>|$)
def valid_email(test='"foo"@bar.com'):
    test = test.rstrip()
    #[^@.]+@[^@.]+[.][^@.]+  <--45%    
    local = "[^.](?P<whole>[\"])?[\da-zA-Z!#$%^&*=?_`{|}~]+(?(whole)[\"])[^.]"
    optional = "([a-zA-Z0-9\-_]{1,62}[.])?"
    hostname = "(?<!-)[0-9a-zA-Z-]{1,63}(?!-)" #cannot start or end with hyphen
    toplevel = "([.][a-zA-Z0-9\-_]{1,62})?(?(whole)[\"])"
    domain = optional + hostname + toplevel
    rgx = '^' + local + '@' + domain + '$'
    rgx = '^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
    #print(rgx)
    search = re.match(rgx, test)
    if search:
        print("true")
    else:
        print("false")

'''local part
!#$%&'*+-/=?^_`{|}~ are allowed 0-9a-zA-Z
s[0] != '.' and s[-1]!= '.' '.' cannot be sequential [.]{2}
quotes are permissable from beginning to end or bound by dot seperators ---."---".--- "---"@
 "(),:;<>@[\] are permissable inside quotes, " and \ must be escaped by \
'''
'''domain part
can be IP address if surrounded by square brackets [IP]
***hostname
0-9a-zA-Z-
s[0] != - and s[-1] != - digits maybe are not allowed
underscore is allowed outside hostname


(?<!...)
Matches if the current position in the string is not preceded by a match
for .... This is called a negative lookbehind assertion. Similar to positive
lookbehind assertions, the contained pattern must only match strings of some
fixed length. Patterns which start with negative lookbehind assertions may
match at the beginning of the string being searched.
'''
