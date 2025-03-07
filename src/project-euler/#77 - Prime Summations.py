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


target = 5000
table = [[0]]
primes = []
i = 0

while table[-1][-1] <= 5000:
    i += 1
    if prime(i+1):
        primes.append(i+1)
        for line in table:
            line.append(line[-1])

    start = 1 if i % 2 == 0 else 0
    table.append([start])
    for vali, val in list(enumerate(primes))[1:]:
        table[i].append(table[i][vali-1])
        if val < i:
            table[i][vali] += table[i-val][vali]
        elif val == i:
            table[i][vali] += 1


print("First number that can be written as a sum of primes in more than %s ways: %s" % (target, i))
