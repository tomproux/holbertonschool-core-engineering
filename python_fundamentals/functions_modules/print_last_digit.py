#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        digit = (-number % 10)
    elif number >= 0 and number < 10:
        print("{}".format(number))
    else:
        digit = number % 10
    print("{}".format())
    return digit
