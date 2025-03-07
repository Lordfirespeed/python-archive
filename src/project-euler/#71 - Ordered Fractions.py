import fractions
from math import gcd
from time import perf_counter

fractionset = []

limit = 1_000_000
target = fractions.Fraction(3, 7)

startd = 2
while target not in fractionset:
    for n in range(1, startd):
        if gcd(n, startd) == 1:
            currfraction = fractions.Fraction(n, startd)
            fractionset.append(currfraction)
    startd += 1

fractionset.sort()
fractionset = fractionset[fractionset.index(target) - 1:]
begin = fractionset[0]

for d in range(startd, limit+1):
    if not d % 10000:
        print("Hit denominator %s" % d)
    beginnumer = int(d * begin)
    endnumer = int(d * target) + 1
    for n in range(beginnumer, endnumer):
        if gcd(n, d) == 1:
            currfraction = fractions.Fraction(n, d)
            fractionset.append(currfraction) #if currfraction not in fractionlist else None
    fractionset.sort()
    fractionset = fractionset[fractionset.index(target) - 1:]
    begin = fractionset[0]


print(begin.numerator)
print("Solution took %s seconds" % perf_counter())
