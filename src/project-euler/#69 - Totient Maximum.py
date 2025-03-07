import math
import traceback

seen = {}


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


def factorise(number):
    factora = 1
    for x in range(number-1, 1, -1):
        if not (number % x):
            factora = x
            break
    factorb = int(number / factora)
    if factorb > factora:
        return [factorb, factora]
    return [factora, factorb]


def primes(number):
    if prime(number) or number <= 1:
        return [number]
    elif number in seen:
        return seen[number]
    factors = factorise(number)
    leftfactors = primes(factors[0])
    rightfactors = primes(factors[1])
    factors = leftfactors + rightfactors
    if number not in seen:
        seen[number] = factors.copy()
    return factors


def totient(n):
    amount = 0
    if prime(n):
        return n - 1
    #factn = primes(n)
    for k in range(1, n+1):
        amount += 1 if math.gcd(k, n) == 1 else 0
        #factk = primes(k)
        #amount += 1 if len(factn + factk) != len(factn) + len(factk) else 0
    return amount


def efficientfindbest(n):
    best = 1
    primen = 1
    done = False
    while not done:
        primen += 1
        if prime(primen):
            if best * primen > n:
                done = True
            else:
                best *= primen
    return best


target = 1000  # 10:6, 100:60, 1000:630, 10000:6930
values = {}

for x in range(1, target+1):
    values[x] = (x/totient(x))
    if not x % 1000:
        print(x)

valueslist = list(values.values())

print("Value of n where n <= %s for which n/phi(n) is a maximum: %s" % (target, list(values.keys())[valueslist.index(max(valueslist))]))
