# This program uses Physics formulas to calculate missing variable #
# v2 - intelligently find and combine formulas #
# Problem: many bugs untested #
# Problem: cannot find common ground between final, initial and intermidiate values #

from sympy import *
init_printing(use_unicode=False)

def calculation (target_var, available_var = dict(), formula_list = list()):

    avail_var_symbols = set()
    for key in available_var.keys(): avail_var_symbols.add(key)

    equation = formula_list[0]
    for scanner in formula_list:
        if (target_var in scanner.free_symbols):
            if (len((scanner.free_symbols).intersection(avail_var_symbols)) >= len((equation.free_symbols).intersection(avail_var_symbols))):
                if (len(scanner.free_symbols) < len(equation.free_symbols)):
                    equation = scanner
    print(' 0 =', equation)

    myDifference = (equation.free_symbols).difference(avail_var_symbols)
    for missing_var in myDifference:
        if (missing_var != target_var):
            equation = equation.subs(missing_var, calculation(missing_var, available_var, formula_list))     #recursive point

    for mySymbol in avail_var_symbols:
        equation = equation.subs(mySymbol, available_var[mySymbol])

    return next(iter(solveset(equation, target_var)))

def main():

    X, x, V_ave, V, v, a, g, t, F_net, F_weight, m = symbols('X x V_ave V v a g t F_net F_weight m', real=True)
    variable_dict = {'X': X, 'x': x, 'V_ave': V_ave, 'V': V, 'v': v, 'a': a, 'g': g, 't': t, 'F_net': F_net, 'F_weight': F_weight, 'm': m}

    formulas = []

    constant_dict = {g: 9.8}    # list of constant variables

    formulas.append(x + (v*t) + (Rational(1,2)*a*(t**Integer(2))) - X)               # [0]
    formulas.append((X - x)/t - V_ave)                                               # [1]
    formulas.append(((V + v)/Integer(2)) - V_ave)                                    # [2]
    formulas.append((V - v)/t - a)                                                   # [3]
    formulas.append(v**Integer(2) + Integer(2)*a*(X - x) - V**Integer(2))            # [4]
    formulas.append(m*a - F_net)                                                     # [5]
    formulas.append(m*g + m*a - F_weight)                                            # [6]

    print('''================================
  ~{Physics Calculator v2}~

     {Variables}
 X - final distance
 x - initial distance
 V_ave - average velocity
 V - final velocity
 v - initial velocity
 a - acceleration
 t - time
 F_net - net force
 F_weight - weight force
 m - mass

     {Equations}
 [0]  X = x + vt + (1/2)a(t^2)
 [1]  V_ave = (X - x)/t
 [2]  V_ave = (V + v)/2
 [3]  a = (V - v)/t
 [4]  V^2 = v^2 + 2a(X - x)
 [5]  F_net = ma
 [6]  F_weight = mg + ma
  ____________________________
 |                            |
 | {Usage}:                   |
 | Enter: (variable value)    |
 | Enter: (target_variable ?) |
 |____________________________|

================================
''')

    userInput_dict = dict()

    while True:

        error = False
        userInput_dict.clear()

        while ('?' not in userInput_dict.values()):
            try: input_symbol, symbol_value = input(' Enter: ').split()
            except ValueError:
                print(' Invalid Input')
                continue;
            if (symbol_value != '?'):
                try: symbol_value = Float(symbol_value)
                except ValueError:
                    print(' Invalid Input')
                    continue;
            userInput_dict[variable_dict[input_symbol]] = symbol_value
        else: del userInput_dict[variable_dict[input_symbol]]

        userInput_dict.update(constant_dict)

        print('\n')
        print(' => Equations used:')

        print('\n ' + '['+ input_symbol + ']', 'equals to:', calculation(variable_dict[input_symbol], userInput_dict, formulas))
        print('\n')
        print('='*32)

        close = input('Would you like to continue [y/n]: ')
        if (close == 'n'):
            print('Program exits')
            break;
        else:
            print('='*32)
            print('\n')

if __name__ == '__main__': main()
