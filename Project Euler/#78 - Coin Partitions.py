from sympy.ntheory import factorint as primefactorise
from collections import defaultdict


def prod(arr):
    v = 1
    for n in arr:
        v *= n
    return v


def powermult(a, b):
    val = defaultdict(lambda: 0)
    for num in a:
        val[num] += a[num]
    for num in b:
        val[num] += b[num]
    return dict(val)


def powerint(val):
    return int(prod([n ** val[n] for n in val]))


def poweradd(a, b):
    return primefactorise(powerint(a) + powerint(b))


target = 1_000
table = [[{1: 1}]]

i = 0
while powerint(table[-1][-1]) == 0 or powerint(table[-1][-1]) % target != 0:
    i += 1
    table.append([{1: 1}])
    for vali, val in zip(range(1, i), range(2, i+1)):
        table[i].append(table[i][vali-1])
        if val <= i:
            try:
                table[i][vali] = poweradd(table[i][vali], table[i-val][vali])
            except IndexError:
                table[i][vali] = poweradd(table[i][vali], table[i-val][-1])
            #print(table[i][vali], table[i-val][vali])
    print(powerint(table[-1][-1]))

print("Least value of n for which p(n) is divisible by %s: %s" % (target, len(table)-1))

# 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56
