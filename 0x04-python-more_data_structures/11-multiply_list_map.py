#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    def mul(value):
        return value * number
    new_list = map(mul, my_list)
    converted_list = list(new_list)
    return converted_list
