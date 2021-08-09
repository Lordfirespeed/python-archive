total = 0
for index in range(1, 1000):
    if not index % 3:
        total += index
    elif not index % 5:
        total += index

print("Total: " + str(total))
