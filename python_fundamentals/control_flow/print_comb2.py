#!/usr/bin/env python3
numbers = list(range(0, 100))
for i in numbers:
    s = str(i)
    if i >= 0 and i < 99:
        if i >= 0 and i < 10:
            s = "0" + s
        print("{}".format(s), end=", ")
    else:
        print("{}".format(s), end="\n")
