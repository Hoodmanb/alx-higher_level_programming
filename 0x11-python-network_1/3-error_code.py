#!/usr/bin/python3
""" a script that takes a url and
    display an error message when an error occur
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    request = Request(argv[1])
    try:
        with urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
