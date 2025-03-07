from itertools import permutations
import fractions

seenbefore = set()
singletwoeng = 0
total = 0
for teams in permutations((True, True, True, True, False, False, False, False)):
    if teams not in seenbefore:
        twoeng = [teams[i] and teams[i+1] for i in range(0, 7, 2)].count(True)
        singletwoeng += 1 if twoeng == 1 else 0
        total += 1
    seenbefore.add(teams)

print(probability := fractions.Fraction(singletwoeng, total))
print(final := int(probability * 4536 + 1))
