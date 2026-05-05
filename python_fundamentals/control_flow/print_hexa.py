#!/usr/bin/env python3
numbers = list(range(0, 99))
for i in numbers:
    hexa = hex(i)
    print("{} = 0x{}".format(i, hexa))
