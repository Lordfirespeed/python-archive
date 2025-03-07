rangemax = 1000
allsolutions = {}
for p in range(10, rangemax+1):
    solutions = []
    for a in range(1, p//2):
        b = p * ((p - (2*a)) / (2*(p - a)))
        c = ((a**2 + b**2) ** 0.5)
        solutions.append([a, int(b), int(c)]) if b.is_integer() and c.is_integer() and c > 0 else None
    [s.sort() for s in solutions]
    solutions = [s for i, s in enumerate(solutions) if solutions.index(s) == i]
    allsolutions[p] = list(solutions)

lengths = [[item[0], len(item[1])][::-1] for item in allsolutions.items()]
print("Value of p which maximises no. of solutions up to %s: %s" % (rangemax, max(lengths)[1]))
