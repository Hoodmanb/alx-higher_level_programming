#!/usr/bin/python3
""" Python script that requests an url and displays
the value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == '__main__':
    try:
        r = requests.get(argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
