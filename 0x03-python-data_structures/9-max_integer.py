#!/usr/bin/python3


def max_integer(my_list=[]):
    y = 0
    if len(my_list) < 1:
        return None
    else:
        for x in my_list:
            if x > y:
                y = x
                continue
            return y
