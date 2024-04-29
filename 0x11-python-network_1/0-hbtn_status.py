#!/usr/bin/python3
"""python script that fetches https://intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        response = res.read()
        print("Body response:")
        print("    - type:", type(response))
        print("    - content:", response)
        print("    - utf8 content:", response.decode("utf-8"))
