target = 100
table = []
for i in range(target+1):
    table.append([1])
    for vali, val in zip(range(1, target), range(2, target+1)):
        table[i].append(table[i][vali-1])
        if val <= i:
            table[i][vali] += table[i-val][vali]

del table[0]

print("Amount of ways %s can be made with sums of 2+ integers: %s" % (target, table[-1][-1] - 1))
