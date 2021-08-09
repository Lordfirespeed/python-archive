from itertools import product
from fractions import Fraction
from sys import exit

upto = 3
found = False
while not found:
    for a, b, c in product(range(-1 * upto, upto+1), repeat=3):
        try:
            x1 = Fraction((c - b), (a - b))
            x2 = Fraction((a - b), (a - c))
            x3 = Fraction((c - a), (b - a))
            x4 = Fraction((b - a), (b - c))
            x5 = Fraction((c - b), (c - a))
            x6 = Fraction((c - a), (c - b))
            vals = [x1, x2, x3, x4, x5, x6]
            final = int(sum([val ** 2 for val in vals]) * 194 + 7)
            if set(list(str(final))) == {"1", "2", "3"} and vals.count(3) == 1:
                print(a, b, c, [str(n) for n in vals], final)
                exit()
        except ZeroDivisionError:
            pass
