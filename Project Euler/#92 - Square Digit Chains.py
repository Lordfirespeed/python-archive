def chain(num):
    if num <= 0:
        return [0]
    seq = [int(num)]
    while 1 not in seq and 89 not in seq:
        seq.append(sum([int(c) ** 2 for c in str(seq[-1])]))
    return seq


target = 10_000_000
amount = 0
for i in range(target):
    amount += 1 if chain(i)[-1] == 89 else 0
    if target > 10000:
        if i % 10000 == 0:
            print("Current i: %s" % i)
