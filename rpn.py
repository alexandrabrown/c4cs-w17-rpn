#!/usr/bin/env python3

# Alexandra Brown
# alexbro
# eecs398 w17 week 10

import operator
import readline
import colored
from colored import stylize


OPERATORS = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
            '^' : operator.pow
            }


def calculate(arg):
    stack = []

    if 'quit' in arg:
        print(stylize('Quitting...', colored.fg('blue_violet')))
        exit(0)

    for op in OPERATORS:
        if op in arg:
            print(stylize(op, colored.fg('blue') +
                          colored.bg('yellow') + colored.attr('bold')))

    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operator_fn = OPERATORS[operand]
            result = operator_fn(arg1, arg2)
            stack.append(result)

    return stack.pop()


def main():
    while True:
        result = calculate(input('rpn calc> '))
        if result < 0:
            result = stylize(result, colored.fg('red'))
        elif result > 0 and result < 1:
            result = stylize(result, colored.fg('green'))
        print('Result:', result)


if __name__ == '__main__':
    main()
