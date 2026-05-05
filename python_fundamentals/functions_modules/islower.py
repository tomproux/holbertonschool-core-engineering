#!/usr/bin/env python3
def islower(c):
    alphabet = list(range(ord('a'), ord('z')))
    if c in alphabet:
        c = chr(c)
        return True
    else:
        return False
