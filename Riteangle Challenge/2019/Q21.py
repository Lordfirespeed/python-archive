from fractions import Fraction

init = [10, 20]
u = init.copy()
v = init.copy()

done = False
while not done:
    u.append(Fraction(u[-1], u[-2]))
    v.append(Fraction((v[-1]+1), v[-2]))
    if u[-1] == v[-1] and u[-2] == v[-2]:
        done = True

print(ans := len(u)-1)
print(final := ans * 74 + 28)
