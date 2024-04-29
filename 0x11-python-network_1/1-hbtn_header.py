#!/usr/bin/python3
"""Python script that takes in a URL, sends a request"""

from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    request = Request(argv[1])
    with urlopen(request) as response:
        print(response.info()['X-Request-Id'])
