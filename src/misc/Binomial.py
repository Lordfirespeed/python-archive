import sympy

a, b, x = sympy.symbols("a b x")
power = 10
expr = (a + b) ** power
print(newexpr := expr.expand())
print(newexpr.subs(a, 1).subs(b, a * x).subs(a, 3/4))
