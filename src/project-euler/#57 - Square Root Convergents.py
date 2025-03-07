from fractions import *


def getnext(frac):
    # if fraction == p/q, the next convergent for root 2 will be (p + 2q) / (p + q)
    p, q = frac.numerator, frac.denominator
    return Fraction((p + 2*q), (p + q))


target = 1000

current = Fraction(1, 1)
amount = 0
for i in range(target):
    current = getnext(current)
    print(current)
    hasproperty = len(str(current.numerator)) > len(str(current.denominator))
    amount += 1 if hasproperty else 0

print("There are %s fractions in the first %s iterations that have a numerator longer than the denominator." % (amount, target))
