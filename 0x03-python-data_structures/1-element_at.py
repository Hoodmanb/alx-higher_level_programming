#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        _list = '{:d}'.format(my_list[idx])
        return _list
