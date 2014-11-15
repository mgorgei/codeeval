def f(n):
    n = int(n)
    if n < 0 or n > 100:
        return "This program is for humans"
    elif n < 3:
        return "Still in Mama's arms"
    elif n < 5:
        return "Preschool Maniac"
    elif n < 12:
        return "Elementary school"
    elif n < 15:
        return "Middle school"
    elif n < 19:
        return "High school"
    elif n < 23:
        return "College"
    elif n < 66:
        return "Working for the man"
    else:
        return "The Golden Years"
        
'''
'Still in Mama's arms'
'Preschool Maniac'
'Elementary school'
'Middle school'
'High school'
'College'
'Working for the man'
'The Golden Years'
"This program is for humans"
'''
