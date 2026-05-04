#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
if number > 0:
    print(number, "is positive")

if number == 0:
    print(number, "is zero")

if number < 0:
    print(number, "is negative")
