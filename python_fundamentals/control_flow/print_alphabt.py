#!/usr/bin/env python3
alphabt = ""

for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter not in ("q", "e"):
        alphabt += letter

print(alphabt)
