import fractions
from math import gcd

limit = 12000
begin = fractions.Fraction(1, 3)
end = fractions.Fraction(1, 2)

between = []

for d in range(2, limit + 1):
    if not d % 250:
        print("Hit denominator %s" % d)
    beginnumer = int(d * begin) + 1
    if d == 2:
        beginnumer = 2
    endnumer = int(d * end)
    for n in range(beginnumer, endnumer+1):
        if gcd(n, d) == 1:
            currfraction = fractions.Fraction(n, d)
            between.append(currfraction)

print(len(between))
