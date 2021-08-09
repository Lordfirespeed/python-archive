from collections import defaultdict
from math import gcd,sqrt

target = 1_500_000
a, b, c = 0, 0, 0
m = 2
result = 0
sums = defaultdict()
sums.default_factory = int
for m in range(2, int(sqrt(target/2)) + 1):
    for n in range(1, m):
        if (n + m) % 2 == 1 and gcd(n, m) == 1:
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            val = a + b + c
            useval = int(val)
            while useval <= target:
                sums[val] += 1
                result += 1 if sums[val] == 1 else 0
                result -= 1 if sums[val] == 2 else 0
                useval += val
    # print("Current max total: %s" % sum(triples[-1]))
    # m += 1
