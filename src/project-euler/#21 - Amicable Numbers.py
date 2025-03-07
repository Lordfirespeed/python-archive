from math import sqrt


def getsumdivisors(number):
    factorpairs = []
    for x in range(1, int(sqrt(number)) + 1):
        if not (number % x):
            factorpairs.append([x, int(number / x)])
    [pair.sort() for pair in factorpairs]
    factorpairs.sort()
    for pair in factorpairs:
        amount = factorpairs.count(pair)
        while amount > 1:
            factorpairs.remove(pair)
            amount = factorpairs.count(pair)
    return sum([value for pair in factorpairs for value in pair if value != number])


amicable = [value for value in range(0, 10000) if value == getsumdivisors(getsumdivisors(value)) and value != getsumdivisors(value)]
print(sum(amicable))
