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


def checkpermu(numlist):
    splitnumlist = [[int(i) for i in list(str(num))] for num in numlist]
    [numlist.sort() for numlist in splitnumlist]
    return splitnumlist.count(splitnumlist[0]) == len(splitnumlist)


primes = [i for i in range(1000, 10000) if efficientprime(i)]

result = False
for prime in primes:
    prime += 1 if prime == 1487 else 0
    for checkprime in [n for n in primes if n > prime]:
        val = ((2 * checkprime) - prime)
        series = [prime, checkprime, val]
        if val in primes and checkpermu(series):
            result = list(series)
            break
    if result:
        break

print("Result: %s" % "".join([str(c) for c in result]))
