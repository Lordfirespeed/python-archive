from math import factorial


def hmmfact(n):
    return sum([factorial(int(x)) for x in str(n)])


def chain(n):
    current = n
    seen = []
    while current not in seen:
        seen.append(current)
        current = hmmfact(current)
    return len(seen)


target = 1_000_000
works = []
for start in range(1, target):
    works.append(start) if chain(start) == 60 else None
    print("Hit start num %s" % start) if not start % 1000 else None



