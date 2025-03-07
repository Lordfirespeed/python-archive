from sympy import sieve
from fractions import Fraction
from itertools import product


primes = sieve

debug = True
target = 50_000_000

primes.extend(int(target ** Fraction(1, 4)))
quartics = [x ** 4 for x in primes._list if x ** 4 < target]
print("Quartics computed") if debug else None
primes.extend(int(target ** Fraction(1, 3)))
cubes = [x ** 3 for x in primes._list if x ** 3 < target]
print("Cubes computed") if debug else None
primes.extend(int(target ** Fraction(1, 2)))
squares = [x ** 2 for x in primes._list if x ** 2 < target]
print("Squares computed") if debug else None

alltotals = set()
for nums in product(squares, cubes, quartics):
    val = sum(nums)
    alltotals.add(val) if val < target else None

print(len(alltotals))
