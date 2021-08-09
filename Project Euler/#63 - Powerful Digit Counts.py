from collections import defaultdict
valid = defaultdict(list)

for n in range(1, 10):
    power = 1
    powerDone = False
    while not powerDone:
        if len(str(n ** power)) == power:
            valid[n].append(n ** power)
            print("%s = %s ** %s" % (n ** power, n, power))
            power += 1
        else:
            powerDone = True

print(sum([len(valid[i]) for i in list(valid.keys())]))

# 1, 2, 3, 4, 5, 6, 7, 8, 9
# 1, 1, 1, 2, 3, 4, 6, 10, 21
