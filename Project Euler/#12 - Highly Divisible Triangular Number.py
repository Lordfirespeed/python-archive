from math import sqrt


def triangular(index):
    naturalnums = list(range(0, index+1))
    return sum(naturalnums)


def getfactors(number):
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
    return [value for pair in factorpairs for value in pair]


currentdivisors = 0
target = 500
numindex = 1000
while not currentdivisors > target:
    value = triangular(numindex)
    currentdivisors = len(getfactors(value))
    if numindex % 100 == 0:
        print("Hit " + str(numindex) + " - " + str(currentdivisors))
    numindex += 1

print(value)
