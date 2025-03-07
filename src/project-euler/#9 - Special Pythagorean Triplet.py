def getfactorpairs(number):
    factorpairs = []
    for x in range(1, number - 1):
        if not (number % x):
            factorpairs.append([x, int(number / x)])
    [pair.sort() for pair in factorpairs]
    factorpairs.sort()
    for pair in factorpairs:
        amount = factorpairs.count(pair)
        while amount > 1:
            factorpairs.remove(pair)
            amount = factorpairs.count(pair)
    return factorpairs


triples = [[3, 4, 5]]
target = 1000
found = False
r = 1
while not found:
    rvalue = r**2 / 2
    if rvalue.is_integer():
        factorpairs = getfactorpairs(int(rvalue))
        for factorpair in factorpairs:
            s = factorpair[0]
            t = factorpair[1]
            x = r + s
            y = r + t
            z = r + s + t
            triples.append([int(x), int(y), int(z)])
            if x + y + z == target:
                found = True
                break
    r += 1

result = triples[-1][0] * triples[-1][1] * triples[-1][2]
print("Result: " + str(result))
