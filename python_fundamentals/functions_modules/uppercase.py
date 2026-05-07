#!/usr/bin/env python3
def uppercase(s):
    result = ""
    for char in s:
        ascii_val = ord(char)
        # Check if character is lowercase letter (a-z)
        if 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += char
    print(result)
