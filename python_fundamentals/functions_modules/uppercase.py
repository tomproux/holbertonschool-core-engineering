#!/usr/bin/env python3
def uppercase(str):
    upper = ""
    for c in str:
        ascii = ord(c)
        if 97 <= ascii <= 122:
            upper += chr(ascii - 32)
        else:
            upper += c
    print("{}".format(upper))
