#!/usr/bin/python3
import sys


def adding_arg():
    added = 0
    for i in range(1, len(sys.argv)):
        added += int(sys.argv[i])
    print(added)


if __name__ == "__main__":
    adding_arg()
