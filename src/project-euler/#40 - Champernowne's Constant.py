targets = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
constant = ""
i = 0
while len(constant) < (max(targets) + 1):
    constant = constant + str(i)
    i += 1

result = 1
for i in targets:
    result *= int(constant[i])

print("Product of the desired indexes of the constant: %s" % result)