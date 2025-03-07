from math import sqrt


def checkabundant(number):
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
    return sum(set([value for pair in factorpairs for value in pair if value != number])) > number


abundants = [index for index in range(0, 28124) if checkabundant(index)]
sums = set([a + b for a in abundants for b in abundants])
resultant = set(range(0, 28124)) - set(sums)
print(sum(resultant))
