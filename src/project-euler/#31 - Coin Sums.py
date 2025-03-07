target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
table = []
for i in range(target+1):
    table.append([1])
    for coini, coin in list(enumerate(coins))[1:]:
        table[i].append(table[i][coini-1])
        if coin <= i:
            table[i][coini] += table[i-coin][coini]

del table[0]

print(table[-1][-1])
