# This program uses Physics formulas to calculate missing variable #

from sympy import *

def calculation (expr = [], symbol_list = []):

    userInput = [j for j in input('Enter [{0}]: '.format(', '.join(str(i) for i in symbol_list))).split()]
    for counter in range(len(userInput)):
        if (userInput[counter] == '?'):
            dict = {'?' : symbol_list[counter]}
        else:
            expr = expr.subs(symbol_list[counter], Float(userInput[counter]))
    print('Answer:', solveset(expr, dict['?']))
    print('=' * 41)

def main():
    X, x, V, v, a, t = symbols('X x V v a t', real=True)

    formula = []
    formula_list = []









#================[Update Here]================#

  #Add list of formulas into the list#
    formula.append(x + v*t + Rational(1,2)*a*(t**Integer(2)) - X)
    formula_list.append([X, x, v, a, t])

    formula.append(v + a*t - V)
    formula_list.append([V, v, a, t])

  #Print list of formulas into console#
    print('''
   Welcome to Physics Calculator v0

=========================================

X - final distance | x - initial distance
V - final velocity | v - initial velocity
a - acceleration   | t - time

    [0]    X = x + vt + (1/2)a(t^2)
    [1]    V = v + at

    [x]    Exit

=========================================''')
#================[Update Here]================#








    while (True):
        userChoice = input('Please choose a formula: ')

        if (userChoice == 'x'): break
        else: calculation (formula[int(userChoice)], formula_list[int(userChoice)])

    print('Program exits')
    print('=' * 41)

if __name__ == '__main__': main()
