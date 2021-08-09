# Can only move DOWN and RIGHT

def array(thing):
    return [x.copy() for x in thing]


with open("#81~83-matrix.txt") as matrixfile:
    valmatrix = [[int(n) for n in line.strip().split(",")] for line in matrixfile.readlines()]
    # reference matrix as 'matrix[y][x]' where Y increases downwards and X increases to the right

totalmatrix = array(valmatrix)

length = len(valmatrix)

for startval in range(1, length*2 - 1):
    maxval = max([n for x in totalmatrix for n in x])
    y = startval if startval < length else 79
    x = 0 if startval < length else startval - 79
    while y >= 0 and x < length:
        #print("Calculating y=%s, x=%s, which has a value of %s." % (y, x, valmatrix[y][x]))
        try:
            if x-1 < 0:
                a = maxval + 1
            else:
                a = totalmatrix[y][x-1]
        except IndexError:
            a = maxval + 1
        try:
            if y-1 < 0:
                b = maxval + 1
            else:
                b = totalmatrix[y-1][x]
        except IndexError:
            b = maxval + 1
        #print(a, b)
        totalmatrix[y][x] = valmatrix[y][x] + min(a, b)
        x += 1
        y -= 1
    # for line in totalmatrix[:5]:
    #     print(line[:5])
    # print()

