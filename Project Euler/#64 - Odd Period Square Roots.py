from math import sqrt


def getseq(n):
    if sqrt(n).is_integer():
        return []

    num = int(sqrt(n))
    print(num)
    seenBefore = []
    sequence = []
    denominator = n - (num ** 2)
    multiplier = 1
    done = False
    while not done:
        nextseq = int((multiplier * (sqrt(n) + num) / denominator))
        sequence.append(nextseq)
        seenBefore.append([int(multiplier), int(num), int(denominator)])
        # print("%s + %s(root + %s) / %s" % (nextseq, multiplier, num, denominator))
        num -= denominator * nextseq

        multiplier = int(denominator)
        denominator = n - (num ** 2)
        if denominator % multiplier == 0:
            denominator /= multiplier
            multiplier = 1

        num *= multiplier * -1
        if [multiplier, num, denominator] in seenBefore:
            if seenBefore.count([multiplier, num, denominator]) == 1:
                done = True

    return sequence


target = 10000
amount = 0
for i in range(target+1):
    amount += 1 if len(getseq(i)) % 2 != 0 else 0

print("Irrational square roots of 0 < N < %s with an odd continued fraction period length: %s" % (target, amount))
