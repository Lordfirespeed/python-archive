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


def lcm(numbera, numberb):
    seta = primes(numbera)
    setb = primes(numberb)
    for number in seta:
        if number in setb:
            setb.remove(number)
    seta += setb
    total = 1
    for number in seta:
        total *= number
    return total


def lcmrange(numbers):
    current = lcm(numbers[0], numbers[1])
    for number in numbers[2:]:
        current = lcm(current, number)
    return current
