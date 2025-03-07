from decimal import *
from math import sqrt as ezsqrt


def checkrational(n):
    return n == round(ezsqrt(n)) ** 2


def accroot(n):
    getcontext().prec = (len(str(int(ezsqrt(n))))) + precision + 1
    val = str(Decimal(n).sqrt())
    return Decimal(val[:val.index(".") + precision])


def getvalue(n):
    squareroot = str(accroot(n))
    values = [int(c) for c in squareroot.replace(".", "")]
    return sum(values)


precision = 100
target = 100
i = 1
total = 0

for x in range(1, target+1):
    if not checkrational(x):
        total += getvalue(x)

print(total)
