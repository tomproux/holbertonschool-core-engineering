#!/usr/bin/env python3
'''alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabt = ""

for letter in alphabet:
    if letter != 'e' and letter != 'q':
        alphabt += letter

print("{}".format(alphabt), end='\n')'''
for lettre in range(ord('a'), ord('z') + 1):
    if chr(lettre) != 'e' and chr(lettre) != 'q':
        print("{}".format(chr(lettre)), end="")
