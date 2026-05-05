#!/usr/bin/env python3
numbers = list(range(0, 100))
for i in numbers:
    print("{}".format(i), end="")
    if i < 99:
        print(", ")
