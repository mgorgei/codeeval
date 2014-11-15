#import operator?
'''
1   ()       Brackets
2   -        Unary minus
3   ^        Exponent
4   *, /     Multiply, Divide (left-to-right precedence)
5   +, -     Add, Subtract (left-to-right precedence)
'''
import re
def f(test='(250+1)'):
    test = test.rstrip('\n')
    print(evaluate(test).format('{:5f}'))

def evaluate(exp):
    if exp.find('-') != -1:
        #distribute unary operator through paranthesis, reverse +/-
        if exp.find('-(') != -1:
            left = exp.find('-(')
            right = exp[left:].find(')')
        #any unary operator switched to a different symbol to treat minus better
    if exp.find('(') != -1:
        left, right = exp.find('('), exp.rfind(')')
        return evaluate(exp[:left] + evaluate(exp[left+1:right]) + exp[right+1:])
    if exp.find('^') != -1:
        pass
    if exp.find('*') != -1:
        mult = exp.find('*')
        '''left of mult(+-/eof) + lhs * rhs + (+-/eof)right of mult '''
        return evaluate( str(data_type(exp[:mult]) * data_type(evaluate(exp[mult + 1:])) ))
    if exp.find('/') != -1:
        pass
    if exp.find('+') != -1:
        plus = exp.find('+')
        '''if exp.count('+') == 1:
            return str(data_type(exp[:plus]) + data_type(exp[plus + 1:]))
        else:'''
        return evaluate( str(data_type(exp[:plus]) + data_type(evaluate(exp[plus + 1:])) ))
    if exp.find('-') != -1:
        pass
    return exp

def data_type(var):
    if var.find('.') != -1:
        return float(var)
    else:
        return int(var)
