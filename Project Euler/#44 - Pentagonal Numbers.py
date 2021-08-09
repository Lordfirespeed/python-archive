def ispentagonal(num):
    return (((1+(24*num))**0.5 + 1) / 6).is_integer()


i = 1
found = False
while not found:
    n = i * (3*i - 1) / 2
    for k in range(1, i):
        m = k * (3*k - 1) / 2
        if ispentagonal(n-m) and ispentagonal(n+m):
            result = int(n-m)
            found = True
            break
    i += 1

print("Result: %s" % result)
