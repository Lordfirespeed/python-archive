def prime(number):
    if number == 1:
        return False
    for x in range(2, number-1):
        if not (number % x):
            return False
    return True


def factorise(number):
    factora = 1
    for x in range(number-1, 2, -1):
        if not (number % x):
            factora = x
            break
    factorb = int(number / factora)
    if factorb > factora:
        return [factorb, factora]
    return [factora, factorb]


def primes(number):
    if prime(number):
        return [number]
    factors = factorise(number)
    leftfactors = primes(factors[0])
    rightfactors = primes(factors[1])
    return leftfactors + rightfactors


def primeindex(findindex):
    primes = []
    index = 1
    while len(primes) < findindex:
        if prime(index):
            primes.append(index)
            if not len(primes) % 100:
                print(len(primes))
        index += 1
    return primes[findindex-1]
