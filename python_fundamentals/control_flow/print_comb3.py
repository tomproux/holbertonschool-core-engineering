numbers = list(range(1, 90))
for i in numbers:
    s = str(i)
    if i >= 1 and i < 89:
        if i >= 0 and i < 10:
            s = "0" + s
        print("{}".format(s), end=", ")
    else:
        print("{}".format(s), end="\n")
