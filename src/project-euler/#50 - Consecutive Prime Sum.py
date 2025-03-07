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


limit = 1_000
maxseqlength = 0
primes = [0] + [n for n in range(limit+1) if efficientprime(n)]
cumulprimes = [primes[0]]
for i in range(1, len(primes)):
    cumulprimes.append(primes[i] + cumulprimes[i-1])

for a in range(maxseqlength, len(cumulprimes)):
    for b in range(a - (maxseqlength+1), -1, -1):
        if cumulprimes[a] - cumulprimes[b] > limit:
            break
        if cumulprimes[a] - cumulprimes[b] in primes and a-b > maxseqlength:
            maxseqlength = a - b
            result = cumulprimes[a] - cumulprimes[b]

print("Prime below %s that can be written as longest sequence of consecutive primes: %s" % (limit, result))
