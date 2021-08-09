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


def truncprime(number):
    number = str(number)
    allprime = True
    for i in range(len(number), 0, -1):
        if not efficientprime(int(number[:i])):
            allprime = False
            break
    if allprime:
        for i in range(1, len(number)):
            if not efficientprime(int(number[i:])):
                allprime = False
                break
    return allprime


truncprimes = []  # number of truncatable primes: eleven. Thus we iterate till we find eleven.
n = 10
while len(truncprimes) < 11:
    truncprimes.append(n) if truncprime(n) else None
    n += 1

print("The sum of the only eleven truncatable primes in both directions: %s" % sum(truncprimes))
