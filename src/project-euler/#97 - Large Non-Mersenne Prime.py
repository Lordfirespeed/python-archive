# 28433 * (2 ** 7830457) + 1
# last x digits


def shorten(num):
    global x
    return int(str(num)[-1 * x:])


x = 10
n = 2
for i in range(7830456):
    n *= 2
    if len(str(n)) > x:
        n = shorten(n)

n *= 28433
print(n)
n = shorten(n)
n += 1
print("Last 10 digits of the large non-Mersenne prime: %s" % n)
