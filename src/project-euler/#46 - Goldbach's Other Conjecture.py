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


primes = [2]

found = False
i = 9
while not found:
    n = max(primes)
    while max(primes) < i:
        n += 1
        primes.append(n) if efficientprime(n) else None

    abides = False
    for prime in primes[:len(primes)-1][::-1]:
        if (((i - prime) / 2) ** 0.5).is_integer():
            abides = True
            break

    if not abides:
        result = i
        found = False
        break
    else:
        i += 2
        while efficientprime(i):
            i += 2

print("Result: %s" % result)
