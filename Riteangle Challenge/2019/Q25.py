import sympy

a, b, c, x = sympy.symbols("a b c x")
formula = (a*x + b/x) ** c + (b*x + c/x) ** a + (c*x + a/x) ** b

target = 1102707270
val = 0
aval = 0
while val != target:
    aval += 1
    bval = aval + 1
    cval = bval + 1
    currform = formula.subs(a, aval).subs(b, bval).subs(c, cval).expand()
    val = sum([arg for arg in currform.args if type(arg) == sympy.numbers.Integer])

print(aval)
print(aval * 474 + 4)
