#!/usr/bin/env python3
numbers = list(range(0, 100))
for i in numbers:
    s = str(i)
    if i >= 0 and i < 10:
        s = "0" + s
    print("{}".format(s), end="")
    if i < 99:
        print(", ", end="")
