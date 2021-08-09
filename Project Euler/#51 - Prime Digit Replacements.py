def change(i, string, substr):
    return string[:i] + substr + string[i+1:]


def pick(x, series):  # Returns all ways of choosing x elements from series
    if x < 1:
        return []
    elif x == 1:
        return [[thing] for thing in series]
    elif x == len(series):
        return [series]
    elif x > len(series):
        return []

    possible = []
    for index, element in enumerate(series):
        newcombos = pick(x-1, series[index+1:])
        [combo.insert(0, element) for combo in newcombos]
        possible += newcombos
    return possible


def pickall(series):
    combinations = []
    for amount in range(len(series)):
        combinations += pick(amount, series)
    return combinations


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


def nextprime(number):
    i = number + 1
    if i % 2 == 0:
        if i == 2:
            return 2
        else:
            i += 1
    while not prime(i):
        i += 2
    return i


target = 8
startindex = 1
index = nextprime(startindex)

currentlength = len(str(index))
indexings = pickall(list(range(currentlength)))

found = False
while not found:
    if currentlength != len(str(index)):
        currentlength = len(str(index))
        indexings = pickall(list(range(currentlength)))

    familyprimes = []
    families = []
    for check in indexings:
        family = []
        for n in range(0, 10):
            num = str(index)
            for changeindex in check:
                num = change(changeindex, num, str(n))
            family.append(int(num)) if len(str(int(num))) == len(str(index)) else None
        #print(index, family)
        amountprime = [prime(n) for n in family].count(True)
        familyprimes.append(amountprime)
        families.append(list(family))

    if target in familyprimes:
        found = True
        break
    else:
        index = nextprime(index)

print("First number to have a %s of 10 prime family: %s" % (target, min(families[familyprimes.index(target)])))
