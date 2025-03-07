import collections
import sys

candidates = []

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


def testSolution(pairDict, values):
    global candidates
    valid = []
    for index, check in enumerate(values):
        valid.append(all([i in pairDict[check] for i in (values[:index] + values[index+1:])]))
    if all(valid):
        candidates.append(values)


def testAllKeys(pairDict):
    for i in sorted(pairDict.keys()):
        for j in pairDict[i]:
            if j > i:
                for m in pairDict[j]:
                    if m > j and m in pairDict[i]:
                        for n in pairDict[m]:
                            if n > m and n in pairDict[j]:
                                for p in pairDict[n]:
                                    if p > n:
                                        testSolution(pairDict, [i, j, m, n, p])


def solution(upper):
    global candidates
    p = [i for i in ([2] + list(range(3, upper, 2))) if prime(i)]
    pairDict = collections.defaultdict(list)
    base = 10
    try:
        for i in range(1, len(p)):
            pi = p[i]
            while base < pi:
                base *= 10
            print(pi, len(pairDict))
            base2 = base
            for j in range(i+1, len(p)):
                pj = p[j]
                while base2 < pj:
                    base2 *= 10
                pipj = pi * base2 + pj
                if prime(pipj):
                    pjpi = pj * base + pi
                    if prime(pjpi):
                        pairDict[pi].append(pj)
                        pairDict[pj].append(pi)
    except KeyboardInterrupt:
        pass
    testAllKeys(pairDict)
    findMinimum = dict([[sum(i), i] for i in candidates])
    minimum = min(findMinimum.keys())
    print(minimum, findMinimum[minimum])


solution(10000)
