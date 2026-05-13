#!/usr/bin/env python3
def pow(a, b):
    result = 1

    if b > 0:
        while b > 0:
            result *= a
            b -= 1
    else:
        while b < 0:
            result /= a
            b += 1

    return float(result)
