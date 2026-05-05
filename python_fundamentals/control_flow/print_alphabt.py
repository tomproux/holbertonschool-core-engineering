#!/usr/bin/env python3
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabt = ""

for letter in alphabet:
    if letter != 'e' and letter != 'q':
        alphabt += letter

print("{}".format(alphabt))
