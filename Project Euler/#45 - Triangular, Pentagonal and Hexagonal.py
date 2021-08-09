def istriangle(x):
    return ((-1 + (1 + 8*x) ** 0.5) / 2).is_integer() or ((-1 - (1 + 8*x) ** 0.5) / 2).is_integer()


def ispenta(x):
    return (((1 + (24 * x)) ** 0.5 + 1) / 6).is_integer()


def ishexa(x):
    return ((-1 - (1 + 8*x) ** 0.5) / 4).is_integer()  #((-1 + (1 + 8*x) ** 0.5) / 4).is_integer()


startT = 285
n = startT
found = False
while not found:
    n += 1
    i = int(n*(n+1) / 2)
    if istriangle(i) and ispenta(i) and ishexa(i):
        found = True
        result = i
        break

print("Result: %s" % result)
