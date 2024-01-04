#!/usr/bin/python3
import sys


def numOfArg():
    number = len(sys.argv) - 1
    _list = sys.argv[1:]
    if number < 1:
        print(0, 'arguments.')
    elif number == 1:
        print(number, 'argument:')
        print('{}: {}'.format(number, _list[0]))
    else:
        print(number, 'arguments:')
        for i in range(number):
            print('{}: {}'.format(i + 1, _list[i]))


if __name__ == "__main__":
    numOfArg()
