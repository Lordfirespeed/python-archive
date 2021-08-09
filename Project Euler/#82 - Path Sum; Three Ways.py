# Can only move UP, DOWN, and RIGHT


def array(nestedlist):
    return [list(thing) for thing in nestedlist]


matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

# with open("#81~83-matrix.txt") as matrixfile:
#     valmatrix = [[int(n) for n in line.strip().split(",")] for line in matrixfile.readlines()]

matrix = list(zip(*matrix))  # rotate the matrix. You can now move DOWN, LEFT, and RIGHT
totalmatrix = array(matrix)

for rowi, row in list(enumerate(totalmatrix))[1:]:
    prevrow = totalmatrix[rowi-1]
    totalmatrix[rowi] = [prevrow[ni] + row[ni] for ni in range(len(row))]
    changed = True
    while changed:
        changed = False
        for ni, n in enumerate(row):
            if ni - 1 >= 0:
                if totalmatrix[rowi][ni - 1] + n < totalmatrix[rowi][ni]:
                    totalmatrix[rowi][ni] = totalmatrix[rowi][ni - 1]
                    changed = True
            if ni + 1 < len(row):
                if totalmatrix[rowi][ni + 1] + n < totalmatrix[rowi][ni]:
                    totalmatrix[rowi][ni] = totalmatrix[rowi][ni + 1]
                    changed = True


from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

finder = AStarFinder()


def pathfind(start, end, matrix):
    global finder
    grid = Grid(matrix=matrix)
    startp = grid.node(*start)
    endp = grid.node(*end)
    path, runs = finder.find_path(startp, endp, grid)
    total = sum([matrix[coord[1]][coord[0]]-1 for coord in path])
    del grid
    return total


with open("#81~83-matrix.txt") as matrixfile:
    matrix = [[int(n) for n in line.strip().split(",")] for line in matrixfile.readlines()]

[line.insert(0, 0) for line in matrix]
[line.append(0) for line in matrix]
matrixwidth, matrixheight = len(matrix[-1]), len(matrix)
[exec("matrix[y][x] += 1") for x in range(matrixwidth) for y in range(matrixheight)]

print(pathfind((0, 0), (matrixwidth-1, matrixheight-1), matrix))
#  for whatever reason this works XD
