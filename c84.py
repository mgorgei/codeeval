def f(test='i am sick today (:(hacker cup: ()started :):))'):
    test = test.rstrip()
    if is_balanced(test):
        print("YES")
    else:
        print("NO")
        
def is_balanced(s):
    left = s.find('(')
    right = s.rfind(')')
    print(s, left,right)
    if left == -1 and right == -1:#no parenthesis
        return True
    
    if left < right:
        return is_balanced(s[left+1:right])
    else:
        return False
#if left == -1 or right == -1:#only way this is valid is if they belong to smileys
#return is_balanced(s.replace(':)', '').replace(':(', ''))
