import fractions
from math import sqrt


def getconvergent(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        return seq[0] + fractions.Fraction(1, getconvergent(seq[1:]))


def trysolution(fract, n):
    x = fract.numerator
    y = fract.denominator
    val = x ** 2 - (n * (y ** 2))
    return val == 1


def findsolution(n):
    if sqrt(n).is_integer():
        return 0

    num = int(sqrt(n))
    sequence = [int(num)]
    denominator = n - (num ** 2)
    multiplier = 1
    found = False
    while not found:
        nextseq = int((multiplier * (sqrt(n) + num) / denominator))
        sequence.append(nextseq)

        convergent = getconvergent(sequence)
        if trysolution(convergent, n):
            return convergent.numerator

        # print("%s + %s(root + %s) / %s" % (nextseq, multiplier, num, denominator))
        num -= denominator * nextseq

        multiplier = int(denominator)
        denominator = n - (num ** 2)
        if denominator % multiplier == 0:
            denominator /= multiplier
            multiplier = 1

        num *= multiplier * -1


target = 1000
maxX = 0
maxXD = 0

for i in range(1, target+1):
    x = findsolution(i)
    if x > maxX:
        maxX, maxXD = x, i

print("Maximum value of x for minimal solutions of D <= %s: %s" % (target, maxXD))
