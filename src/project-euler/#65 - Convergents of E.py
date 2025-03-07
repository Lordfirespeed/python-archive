import fractions
from math import sqrt

convergent = 100


def geteseq(length):
    seq = [2]
    k = 1
    while len(seq) < length:
        seq += [1, 2 * k, 1]
        k += 1
    return seq[:length]


def getconvergent(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        return seq[0] + fractions.Fraction(1, getconvergent(seq[1:]))


digits = [int(c) for c in str(getconvergent(geteseq(convergent)).numerator)]
print("Sum of numerator digits of %s convergent of E: %s" % (convergent, sum(digits)))
