#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastDigit = number % 10
_str = "Last digit of {} is {}".format(number, lastDigit)

if lastDigit > 5:
    print(_str, "and is greater than 5")
elif lastDigit == 0:
    print(_str, "and is 0")
else:
    print(_str, "and is less than 6 and not 0")
