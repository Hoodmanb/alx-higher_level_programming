#!/usr/bin/python3

"""a func that reads a text files and prints"""


def read_file(filename=""):
    """open and read file using with"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
