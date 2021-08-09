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


def circularprime(number):
    number = str(number)
    allprime = True
    for i in range(len(number)):
        if not efficientprime(int(number[i:] + number[:i])):
            allprime = False
            break
    return allprime


target = 1_000_000
values = []
for i in range(target+1):
    values.append(i) if circularprime(i) else None

print("Circular primes below %s: %s" % (target, len(values)))
