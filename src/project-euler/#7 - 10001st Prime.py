def prime(number):
    if number == 1:
        return False
    for x in range(2, number-1):
        if not (number % x):
            return False
    return True


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


print(primeindex(10001))
