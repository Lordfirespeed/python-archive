import sympy
x, y, z, a, b, c = sympy.symbols("x y z a b c")


def leftriemanneq(eq, strips, low, high):
    stripsize = (high-low)/strips
    tablevals = []
    i = low
    while i > high:
        tablevals.append((i, eq.subs(x, i)))  
        i -= stripsize
    return leftriemanntable(tablevals)


def rightriemanneq(eq, strips, low, high):
    stripsize = (high-low)/strips
    tablevals = []
    i = low
    while i > high:
        tablevals.append((i, eq.subs(x, i)))  
        i -= stripsize
    return rightriemanntable(tablevals)


def leftriemanntable(tablevals):
    tablevals = sorted(tablevals)
    return sympy.nsimplify(sum([tablevals[i][1]*abs(tablevals[i+1][0]-tablevals[i][0]) for i in range(len(tablevals)-1)]))


def rightriemanntable(tablevals):
    tablevals = sorted(tablevals)
    return sympy.nsimplify(sum([tablevals[i][1]*abs(tablevals[i][0]-tablevals[i-1][0]) for i in range(len(tablevals)-1, 0, -1)]))
