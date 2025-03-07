def checkwin(grid, width, height):
    # check horizontal (-) wins
    for x in range(width - 3):
        for y in range(height):
            try:
                vals = []
                vals.append(grid[x][y])
                vals.append(grid[x+1][y])
                vals.append(grid[x+2][y])
                vals.append(grid[x+3][y])
                if len(set(vals)) <= 1:
                    indexes = [(x, y), (x+1, y), (x+2, y), (x+3, y)]
                    return [True, indexes]
            except IndexError:
                pass

    # check vertical (|) wins
    for x in range(width):
        for y in range(height - 3):
            try:
                vals = []
                vals.append(grid[x][y])
                vals.append(grid[x][y+1])
                vals.append(grid[x][y+2])
                vals.append(grid[x][y+3])
                if len(set(vals)) <= 1:
                    indexes = [(x, y), (x, y+1), (x, y+2), (x, y+3)]
                    return [True, indexes]
            except IndexError:
                pass

    # check diagonal (/) wins
    for x in range(width - 3):
        for y in range(height - 3):
            try:
                vals = []
                vals.append(grid[x][y])
                vals.append(grid[x+1][y+1])
                vals.append(grid[x+2][y+2])
                vals.append(grid[x+3][y+3])
                if len(set(vals)) <= 1:
                    indexes = [(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)]
                    return [True, indexes]
            except IndexError:
                pass

    # check diagonal (\) wins
    for x in range(width - 3):
        for y in range(3, height):
            try:
                vals = []
                vals.append(grid[x][y])
                vals.append(grid[x+1][y-1])
                vals.append(grid[x+2][y-2])
                vals.append(grid[x+3][y-3])
                if len(set(vals)) <= 1:
                    indexes = [(x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)]
                    return [True, indexes]
            except IndexError:
                pass

    return [False, []]
