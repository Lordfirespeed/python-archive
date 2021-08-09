from fractions import Fraction


def getnumber(x, n):
    if n == 0:
        return 0
    return n * (x ** n) + getnumber(x, n-1)


a = Fraction(1, 8)
prevfinal, final, n = 0, 1, 1
while final != prevfinal:
    prevfinal = final
    val = getnumber(a, n)
    final = int(val * 8091 + 1)
    n += 1
print(final)
