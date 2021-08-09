def nextiter(n):
    return n + int(str(n)[::-1])


def checkpalin(n):
    s = str(n)
    return s == s[::-1]


def checklychrel(n):
    current = n
    for i in range(50):
        current = nextiter(current)
        if checkpalin(current):
            return False
    return True


target = 10_000
amount = 0
for i in range(10, target+1):
    amount += 1 if checklychrel(i) else 0

print("There are %s Lychrel numbers under %s." % (amount, target))