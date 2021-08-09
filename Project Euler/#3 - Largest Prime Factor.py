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
    if prime(number):
        return [number]
    factors = factorise(number)
    leftfactors = primes(factors[0])
    rightfactors = primes(factors[1])
    return leftfactors + rightfactors


inputnumber = 600851475143
factors = primes(inputnumber)
print(factors)
