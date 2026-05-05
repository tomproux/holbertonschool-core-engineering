#!/usr/bin/env python3
numbers = list(range(0, 100))
for i in numbers:
    s = str(i)
    if i == 99:
        s = s + "\n"
    elif i >= 0 and i < 10:
        s = "0" + s
    else:
        print(", ", end="")
    print("{}".format(s), end="")
