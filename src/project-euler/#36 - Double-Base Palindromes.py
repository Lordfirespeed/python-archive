target = 1_000_000
values = []
for i in range(target):
    values.append(i) if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1] else None

print("Sum of double-base palindromes between 0 and %s: %s" % (target, sum(values)))
