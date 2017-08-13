# This program uses Physics formulas to calculate missing variable #
# v1 - organize list of symbols in an expression lexicographically #
# v1 - catch any invalid outputs from user #
# v1 - print usage instruction #

from sympy import *

def calculation (expr = []):
    symbol_list = list(ordered(expr.free_symbols))
    target_dict = {}
    userInput = [j for j in input('Enter [{0}]: '.format(', '.join(str(i) for i in symbol_list))).split()]
    for counter in range(len(userInput)):
        if (userInput[counter] == '?'):
            target_dict = {'?' : symbol_list[counter]}
        else:
            try: Float(userInput[counter])
            except ValueError: continue
            expr = expr.subs(symbol_list[counter], Float(userInput[counter]))
    if ('?' in target_dict):
        print('Answer:', solveset(expr, target_dict['?']))
        print('\n')
        print('=' * 41)
        print('\n')
    else: 
        print('''
  ___________________________
 |                           |
 | Invalid input: missing '?'|
 |___________________________|
        ''')
        print('=' * 41)
        print('\n')

def main():
    X, x, V, v, a, t = symbols('X x V v a t', real=True)

    formula = []
    formula_list = []










#================[Update Here]================#

          #Add list of formulas into the list#
    formula.append(x + v*t + Rational(1,2)*a*(t**Integer(2)) - X)               # [0]
    formula.append((X - x)/t - V)                                               # [1]
    formula.append(v + a*t - V)                                                 # [2]
    formula.append(v**Integer(2) + Integer(2)*a*(X - x) - V**Integer(2))        # [3]
    formula.append((V - v)/t - a)                                               # [4]

          #Print list of formulas into console#
    print('''
     Welcome to Physics Calculator v1

=========================================

X - final distance | x - initial distance
V - final velocity | v - initial velocity
a - acceleration   | t - time

    [0]    X = x + vt + (1/2)a(t^2)
    [1]    V = (X - x)/t
    [2]    V = v + at
    [3]    V^2 = v^2 + 2a(X - x)
    [4]    a = (V - v)/t

    [x]    Exit
  _____________________________________
 |                                     |
 | Usage:                              |
 |-Enter ? to indicate target variable.|
 |-Enter numbers to known variables.   |
 |-Enter non-numbers to pass variables.|
 |_____________________________________|

=========================================
    ''')
#================[Update Here]================#









    while (True):
        userChoice = input('Please choose a formula: ')
        if (userChoice == 'x'): break
        else: calculation (formula[int(userChoice)])

    print('Program exits')
    print('\n')
    print('=' * 41)

if __name__ == '__main__': main()
