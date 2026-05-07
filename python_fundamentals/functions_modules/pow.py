#!/usr/bin/env python3
def pow(a, b):
    result = 1
    for c in range(b):
        result = a * (a ^ b)
    print("{}".format(result))
    return result
