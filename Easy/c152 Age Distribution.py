'''AGE DISTRIBUTION

You're responsible for providing a demographic report for your local school
district based on age. To do this, you're going determine which 'category' each
person fits into based on their age.
The person's age will determine which category they should be in:

If they're from 0 to 2 the child should be with parents print : 'Still in Mama'sarms' 
If they're 3 or 4 and should be in preschool print : 'Preschool Maniac' 
If they're from 5 to 11 and should be in elementary school print : 'Elementary school' 
From 12 to 14: 'Middle school' 
From 15 to 18: 'High school' 
From 19 to 22: 'College'
From 23 to 65: 'Working for the man' 
From 66 to 100: 'The Golden Years' 
If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans"

INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
of input contains one integer - age of the person:
0
19

OUTPUT SAMPLE:
For each line of input print out where the person is:
Still in Mama's arms
College
'''
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
