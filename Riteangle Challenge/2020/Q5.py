# a + ar + ar^2 + ar^3 -> a(1 + r + r^2 + r^3) = 360
# 10a is an integer -> a can be any real positive number to 1dp 0<=a<=360

from sympy import symbols, solve, sympify

r, a, b, c, d, varyinga = symbols("r a b c d A")
eq = r + r**2 + r**3 - (360/varyinga) + 1


def getsols(varyingaval):
    solutions = solve(eq.subs(varyinga, varyingaval))
    return [sol for sol in solutions if sympify(sol).is_real and float(sol).is_integer()]


correctaval = None
correctsol = None
for varyingaval in range(1, 3600):
    varyingaval /= 10
    sols = getsols(varyingaval)
    if len(sols) > 0:
        correctaval = varyingaval
        correctsol = max(sols)
        break


print(f"r = {int(correctsol)}, a = {correctaval}")
print(f"Final = {int(correctaval * 2812 + 1)}")

