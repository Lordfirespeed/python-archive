from itertools import product


def checkgrid(grid):
    global xrange, yrange
    foundval = 0
    for y in range(yrange-1):
        for x in range(xrange-1):
            total = grid[y][x] + grid[y+1][x] + grid[y][x+1] + grid[y+1][x+1]
            if foundval == 0:
                foundval = total
            else:
                if foundval != total:
                    return False
    return True


xrange, yrange = 6, 5

grid = [[0 for x in range(xrange)] for y in range(yrange)]

known = [((0, 4), 9), ((2, 1), 2), ((2, 2), 5), ((3, 2), 8), ((3, 3), 7), ((4, 0), 5), ((4, 4), 9), ((4, 5), 6)]
for loc, val in known:
    grid[loc[0]][loc[1]] = val

unknown = [(y, x) for y in range(yrange) for x in range(xrange)]
[unknown.remove(loc) for loc, val in known]

currcheckto = max([val for loc, val in known])
currgrid = [line.copy() for line in grid]
done = False
while not done:
    for allinsvals in product(range(currcheckto), repeat=len(unknown)):
        inserts = zip(unknown, allinsvals)
        for loc, val in inserts:
            currgrid[loc[0]][loc[1]] = val
        if checkgrid(currgrid):
            done = True
            break
    currcheckto += 1
    print(f"Currcheckto: {currcheckto}")

print(currgrid[0][0], currgrid[0][5])
