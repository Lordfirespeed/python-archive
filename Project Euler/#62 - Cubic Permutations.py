from math import ceil
import itertools

target = 5


def iscube(n):
    cbrt = n ** (1/3)
    rounded = round(cbrt)
    return rounded ** 3 == n


def getvalues(n):
    return [str(n).count(str(x)) for x in range(0, 10)]


def getcubes(values):
    indices = [i for i, x in enumerate(list(currentCubes.values())) if x == values]
    return [list(currentCubes.keys())[index] for index in indices]


n = 0
currentCubes = {}
found = False
while not found:
    currentCubeNum = n ** 3
    currentCubes[currentCubeNum] = getvalues(currentCubeNum)
    currentCubes = dict([[num, currentCubes[num]] for num in currentCubes.keys() if len(str(num)) == len(str(n ** 3))])
    print("Current maximum cube index: %s" % n)

    permCubes = getcubes(currentCubes[currentCubeNum])
    if len(permCubes) == target:
        value = min(permCubes)
        found = True
        break

    n += 1


print("Smallest cube for which exactly %s of its permutations are cubic: %s" % (target, value))
