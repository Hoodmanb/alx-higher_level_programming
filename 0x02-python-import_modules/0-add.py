#!/usr/bin/python3
from add_0 import add


def main():
    a = 1
    b = 2
    addn = add(a, b)
    return print('{} + {} = {}'.format(a, b, addn))


if __name__ == "__main__":
    main()
