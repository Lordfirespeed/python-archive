from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

finder = AStarFinder()


def pathfind(start, end, matrix):
    global finder
    grid = Grid(matrix=matrix)
    startp = grid.node(*start)
    endp = grid.node(*end)
    path, runs = finder.find_path(startp, endp, grid)
    total = sum([matrix[coord[1]][coord[0]] for coord in path])
    del grid
    return total


with open("#81~83-matrix.txt") as matrixfile:
    matrix = [[int(n) for n in line.strip().split(",")] for line in matrixfile.readlines()]

matrixwidth, matrixheight = len(matrix[-1]), len(matrix)

print(pathfind((0, 0), (matrixwidth-1, matrixheight-1), matrix))
