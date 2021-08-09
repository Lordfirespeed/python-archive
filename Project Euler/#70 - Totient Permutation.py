from time import perf_counter


def checkpermu(numlist):
    splitnumlist = [[int(i) for i in list(str(num))] for num in numlist]
    [numlist.sort() for numlist in splitnumlist]
    return splitnumlist.count(splitnumlist[0]) == len(splitnumlist)


start = perf_counter()

target = 10 ** 7  # 10,000,000
phi = list(range(target))
for n in range(2, target):
    if phi[n] == n:
        multiplier = (1-1/n)
        for multiple in range(n, target, n):
            phi[multiple] = round(phi[multiple] * multiplier)

arepermutations = {}
for i in range(2, target):
    if checkpermu((i, phi[i])):
        arepermutations[i] = i/phi[i]

values = list(arepermutations.values())
solution = list(arepermutations.keys())[values.index(min(values))]
end = perf_counter()
time = str(end-start)
time = time[:time.index(".")+4]
print("Computed solution: %s in %s seconds." % (solution, time))
