#!/usr/bin/python3
#for i in range(122, 97):
for i in range(122, 96, -1):
    if i % 2 != 0:
        chr(i).upper()
    print(f"{i}")
