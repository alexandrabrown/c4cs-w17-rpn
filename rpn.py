#!/usr/bin/env python3

# Alexandra Brown
# alexbro
# eecs398 w17 week 10

import operator

OPERATORS = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
            }

def calculate(arg):
    stack = []

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
        print('Result:', result)

if __name__ == '__main__':
    main()
