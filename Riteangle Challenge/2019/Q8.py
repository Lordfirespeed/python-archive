import itertools
import fractions


def validate(n):
    if n < 0:
        return n + 30
    elif n > 30:
        return n - 30
    else:
        return n


def simulate(AWay, BWay, CWay):
    A = fractions.Fraction(0)
    B = fractions.Fraction(10)
    C = fractions.Fraction(20)

    ASpeed = fractions.Fraction(1, 6)
    BSpeed = fractions.Fraction(2, 6)
    CSpeed = fractions.Fraction(3, 6)

    if not AWay:
        ASpeed *= -1
    if not BWay:
        BSpeed *= -1
    if not CWay:
        CSpeed *= -1

    thirdseconds = 0
    while True:
        A += ASpeed
        B += BSpeed
        C += CSpeed

        A = validate(A)
        B = validate(B)
        C = validate(C)

        thirdseconds += 1

        ATup, BTup, CTup = (A, "A"), (B, "B"), (C, "C")
        order = "".join([tup[1] for tup in sorted([ATup, BTup, CTup])])
        if order not in ["ABC", "CAB", "BCA"] or A == B or B == C or A == C:
            if A == B or B == C or A == C:
                return thirdseconds
            else:
                print("Not accurate enough - found an overtake/passby rather than a collision.\n", A, B, C, AWay, BWay, CWay)
                return thirdseconds


times = []
for ways in itertools.product([True, False], repeat=3):
    time = simulate(*ways)
    times.append(time)

average = (sum(times) / len(times)) / 6
print(average)

