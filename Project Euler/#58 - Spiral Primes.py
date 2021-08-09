from math import sqrt


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


def nexttopright(value):
    n = (sqrt(value) - 1) / 2
    return int((2*(n+1) + 1) ** 2)


def nextbotright(value):
    n = (sqrt(4*value - 3) + 1) / 4
    return int(4*((n+1) ** 2) - 2*(n+1) + 1)


def nextbotleft(value):
    n = (sqrt(value - 1)) / 2
    return int(4*((n+1)**2) + 1)


def nexttopleft(value):
    n = (sqrt(4*value - 3) - 1) / 4
    return int(4*((n+1) ** 2) + 2*(n+1) + 1)


target = 10

spiralsize = 7 # initial spiral size
seqlength = (spiralsize // 2) + 1  # length of diagonals from centre given spiral size

topright = [(2*n + 1)**2 for n in range(seqlength)]  # sequence (2n+1)^2 OR 4n^2 + 4n + 1
botright = [(4*(n**2) - 2*n + 1) for n in range(1, seqlength)]  # sequence 4n^2 - 2n + 1
botleft = [(4*(n**2) + 1) for n in range(1, seqlength)]  # sequence 4n^2 + 1
topleft = [(4*(n**2) + 2*n + 1) for n in range(1, seqlength)]  # sequence 4n^2 + 2n +1

toprightp = [prime(v) for v in topright]
botrightp = [prime(v) for v in botright]
botleftp = [prime(v) for v in botleft]
topleftp = [prime(v) for v in topleft]

currentsize = spiralsize
found = False
while not found:
    allpbools = list(toprightp) + list(botrightp) + list(botleftp) + list(topleftp)
    noprime, total = allpbools.count(True), len(allpbools)
    ratiopercent = noprime / total * 100
    if ratiopercent < target:
        found = True
        break
    else:
        currentsize += 2
        topright.append(nexttopright(topright[-1]))
        botright.append(nextbotright(botright[-1]))
        botleft.append(nextbotleft(botleft[-1]))
        topleft.append(nexttopleft(topleft[-1]))

        toprightp.append(prime(topright[-1]))
        botrightp.append(prime(botright[-1]))
        botleftp.append(prime(botleft[-1]))
        topleftp.append(prime(topleft[-1]))

print("First spiral side length to have 10 percent or fewer primes along diagonals: %s" % currentsize)
