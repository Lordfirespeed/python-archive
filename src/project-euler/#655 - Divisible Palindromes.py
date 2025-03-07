value = 109
target = 100000

# value = 1_000_019
# target = 10 ** 32


def genpalindromes(prevpalindromes=[], evenlen=False):
    if len(prevpalindromes) == 0:
        if evenlen:
            return [str(n) * 2 for n in range(1, 10)]
        else:
            return [str(n) for n in range(1, 10)]

    return [str(n) + nested + str(n) for nested in prevpalindromes for n in range(1, 10)]


def findall():
    global value
    global target

    startlen = len(str(value))
    endlen = len(str(target))

    evenpalindromes = genpalindromes([], True)
    oddpalindromes = genpalindromes([], False)

    for length in range(3, startlen):
        if length % 2 == 0:
            evenpalindromes = genpalindromes(evenpalindromes)
        else:
            oddpalindromes = genpalindromes(oddpalindromes)

    good = []
    for pallength in range(startlen, endlen):
        if pallength % 2 == 0:
            evenpalindromes = genpalindromes(evenpalindromes)
            good += [pal for pal in evenpalindromes if int(pal) % value == 0]
        else:
            oddpalindromes = genpalindromes(oddpalindromes)
            good += [pal for pal in oddpalindromes if int(pal) % value == 0]

    return good


def finddivisibles():
    global value
    i = 1
    valid = []
    done = False
    while not done:
        try:
            valid.append(i * value)
            i += 1
        except KeyboardInterrupt:
            done = True
    return valid


def sumdigits(num):
    return sum([int(c) for c in str(num)])


# for x in range(41):
#     y = x * 1_000_019
#     print(x, y, sumdigits(y))
