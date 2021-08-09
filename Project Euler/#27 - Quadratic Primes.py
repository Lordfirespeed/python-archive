def prime(number):
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


def isprime(number):
    global primes
    i = 0
    while primes[i] <= number:
        if primes[i] == number:
            return True
    return False


primes = [i for i in range(87401) if prime(i)]
bs = [i for i in range(1001) if prime(i)]
#print("Generated primes.")

amax, bmax, nmax = 0, 0, 0
for a in range(-999, 1001, 2):
    for bi in range(1, len(bs)):
        for sign in [1, -1]:
            n = 0
            if bs[bi] == 2:
                while (n ** 2 + (a-1) * n + sign * bs[bi]) in primes:
                    n += 1

                if n > nmax:
                    amax = a
                    bmax = bs[bi]
                    nmax = n

            while (n**2 + a*n + sign*bs[bi]) in primes:
                n += 1

            if n > nmax:
                amax = a
                bmax = bs[bi]
                nmax = n

print("A: %s, B: %s forms a sequence of length %s. Product is %s." % (amax, bmax, nmax, amax*bmax))
