from math import factorial


def c(n, r):
    if not r <= n:
        return 0
    return factorial(n) / (factorial(r) * factorial(n - r))


target = 100
over = 1_000_000

amount = 0
for n_num in range(1,target+1):
    for r_num in range(n_num, 0, -1):
        value = c(n_num, r_num)
        if value > over:
            amount += 1

print("Amount of values for nCr for 1<=n<=%s that are over %s: %s" % (target, over, amount))
