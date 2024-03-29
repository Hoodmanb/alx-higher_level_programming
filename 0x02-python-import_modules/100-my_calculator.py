#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def cal_():
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in ['+', '-', '/', '*']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op == '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        elif op == '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif op == '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        elif op == '/':
            print('{} / {} = {}'.format(a, b, div(a, b)))


if __name__ == "__main__":
    cal_()
