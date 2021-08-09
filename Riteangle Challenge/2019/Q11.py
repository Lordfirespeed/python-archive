from itertools import product
from sys import exit


def friendly(a, b):
    return a[0] == b[1] and b[0] == a[1]


def selffriendly(a):
    return a[0] == a[1]


distinct = set()

for vals in product(range(1, 100), repeat=4):
    RectAArea = vals[0] * vals[1]
    RectBArea = vals[2] * vals[3]
    RectAPeri = 2 * vals[0] + 2 * vals[1]
    RectBPeri = 2 * vals[2] + 2 * vals[3]
    RectA, RectB = (RectAArea, RectAPeri), (RectBArea, RectBPeri)
    if friendly(RectA, RectB):
        distinct = distinct.union(set(vals))
    else:
        distinct = distinct.union({vals[0], vals[1]}) if (x := selffriendly(RectA)) else distinct
        distinct = distinct.union({vals[2], vals[3]}) if (y := selffriendly(RectB)) else distinct

print(total := sum(distinct))
print(total * 6 + 129)
