def prime(number):
    if number == 1:
        return False
    for x in range(2, number-1):
        if not (number % x):
            return False
    return True


def efficientprime(number):
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


primes = [index for index in range(0, 2_000_000) if efficientprime(index)]
print(sum(primes))
