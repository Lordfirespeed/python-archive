gridsize = 20
gridsize += 1

grid = [[0 for x in range(gridsize)] for y in range(gridsize)]
# grid should be referenced as grid[y][x]

for currentrowcolumn in range(gridsize):
    for x in range(currentrowcolumn, gridsize):
        if currentrowcolumn - 1 < 0:
            abovevalue = 0
        else:
            abovevalue = grid[currentrowcolumn-1][x]
        if x - 1 < 0:
            leftvalue = 1
        else:
            leftvalue = grid[currentrowcolumn][x-1]
        grid[currentrowcolumn][x] = leftvalue + abovevalue

    for y in range(currentrowcolumn+1, gridsize):
        if y - 1 < 0:
            abovevalue = 1
        else:
            abovevalue = grid[y-1][currentrowcolumn]
        if currentrowcolumn - 1 < 0:
            leftvalue = 0
        else:
            leftvalue = grid[y][currentrowcolumn-1]
        grid[y][currentrowcolumn] = leftvalue + abovevalue

print("Result: " + str(grid[-1][-1]))
