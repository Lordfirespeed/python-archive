limit = 1_000_000
result = 0

phi = list(range(limit+1))
for n in range(2, limit+1):
    if phi[n] == n:
        multiplier = (1-1/n)
        for multiple in range(n, limit+1, n):
            phi[multiple] = round(phi[multiple] * multiplier)

result = sum(phi[2:])

print(result)

