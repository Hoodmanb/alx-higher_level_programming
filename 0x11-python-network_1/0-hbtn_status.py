#!/usr/bin/python3
"""python script that fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen, Request

if __name__ == "__main__":
    request = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(request) as res:
        response = res.read()
        print("Body response:")
        print(" - type:", type(response))
        print(" - content:", response)
        print(" - utf8 content:", response.decode("utf-8"))
