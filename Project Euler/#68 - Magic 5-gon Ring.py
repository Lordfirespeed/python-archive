from itertools import permutations

gon = 5
target = 16
values = range(1, (2*gon) + 1)
solutions = []

for midnums in permutations(values, gon):
    outers = list(set(values) - set(midnums))

    trymid = list(midnums) + [midnums[0]]
    for tryouter in permutations(outers):
        if tryouter[0] == min(tryouter):
            lines = [[tryouter[i]] + trymid[i:i+2] for i in range(gon)]
            checksum = sum(lines[0])
            if all([sum(line) == checksum for line in lines[1:]]):
                if lines not in solutions:
                    solutions.append(lines)

stringnums = [int(n) for n in ["".join(["".join([str(c) for c in line]) for line in lines]) for lines in solutions]]
stringnums = [n for n in stringnums if len(str(n)) == target]
print("Maximum numstring of length %s for a %s-gon ring: %s" % (target, gon, max(stringnums)))
