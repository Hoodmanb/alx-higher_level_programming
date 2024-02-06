#!/usr/bin/python3

"""a function that writes to a file and return"""


def write_file(filename="", text=""):
    """open a file, wtite to it and return the
    num of char wtitten"""

    with open(filename, 'w', encoding='utf-8')
    as file:
        return file.write(text)
