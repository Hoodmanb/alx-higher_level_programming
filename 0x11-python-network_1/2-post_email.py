#!/usr/bin/python3
"""A python script that takes in a URL and email
   send a post request with the email as a parameter
   and displays the body of the response
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    email = "email=" + argv[2]
    email = email.encode('ascii')
    request = Request(argv[1], email)
    with urlopen(request) as response:
        body = response.read
        print(body.decode('utf-8'))
