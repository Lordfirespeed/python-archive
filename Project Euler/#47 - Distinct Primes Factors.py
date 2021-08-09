def prime(number):
    if number == 1:
        return False
    for x in range(2, number-1):
        if not (number % x):
            return False
    return True


def factorise(number):
    factora = 1
    for x in range(2, number-1):
        if not (number % x):
            factora = x
            break
    factorb = int(number / factora)
    if factorb > factora:
        return [factorb, factora]
    return [factora, factorb]


def primes(number):
    if prime(number) or number == 1:
        return [number]
    factors = factorise(number)
    leftfactors = primes(factors[0])
    rightfactors = primes(factors[1])
    return leftfactors + rightfactors


target = 4
found = False
i = 1
while not found:
    i += 1
    factors = [primes(n) for n in range(i, i+target)]
    factordicts = [dict([[n, listprimes.count(n)] for n in listprimes]) for listprimes in factors]
    found = True
    for factordict in factordicts:
        found = False if len(factordict) != target else found
    for dictindex in range(len(factordicts)):
        if not found:
            break
        checkindexes = list(range(len(factordicts)))
        checkindexes.remove(dictindex)
        for checki in checkindexes:
            if not found:
                break
            for primen in factordicts[dictindex]:
                try:
                    if factordicts[dictindex][primen] == factordicts[checki][primen]:
                        found = False
                        break
                except KeyError:
                    pass

    if i % 2500 == 0:
        print("Hit index %s." % i)

resultstr = ", ".join([str(c) for c in range(i, i+target)])
print("First %s numbers to have %s distinct prime factors: %s" % (target, target, resultstr))

for pindex, n in enumerate(range(i, i+target)):
    msg = str(n) + ": "
    for factor in factordicts[pindex]:
        msg += (str(factor)+"^"+str(factordicts[pindex][factor]) if factordicts[pindex][factor] != 1 else str(factor))
        msg += ", "
    print(msg[:-2])
