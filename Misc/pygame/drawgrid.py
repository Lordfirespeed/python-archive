import pygame

grid = []

def drawgrid(surface, size, rows, columns):
    vertstart = size[0] / 14
    vertlinegap = (size[0] - (vertstart * 2)) / columns

    horistart = size[1] / 20
    horilinegap = (size[1] - (horistart * 2)) / rows
    
    for vertline in range(columns + 1):
        startpos = vertstart + (vertline * vertlinegap)
        pygame.draw.line(surface, (255, 255, 255), (startpos, horistart), (startpos, (size[1]-horistart)))
        
    for horiline in range(rows + 1):
        startpos = horistart + (horiline * horilinegap)
        pygame.draw.line(surface, (255, 255, 255), (vertstart, startpos), ((size[0]-vertstart), startpos))

    horigridsize = size[0] - (vertstart * 2)
    vertgridsize = size[1] - (horistart * 2)
    
    return [vertstart, vertlinegap, horigridsize, horistart, horilinegap, vertgridsize]

def drawsquaregrid(surface, size, rows):
    gridsize = min(size) - (min(size) / 10)

    vertstart = (size[0] - gridsize) / 2
    horistart = (size[1] - gridsize) / 2
    linegap = gridsize / rows

    for vertline in range(rows + 1):
        startpos = vertstart + (vertline * linegap)
        pygame.draw.line(surface, (255, 255, 255), (startpos, horistart), (startpos, (horistart + gridsize)), 1)

    for horiline in range(rows + 1):
        startpos = horistart + (horiline * linegap)
        pygame.draw.line(surface, (255, 255, 255), (vertstart, startpos), ((vertstart + gridsize), startpos), 1)

    horigridsize = rows * linegap
    return [vertstart, linegap, gridsize, horistart, linegap, gridsize]

def coordsgrid(grid, gridx, gridy):
    #finds centre of grid's x, y in terms of the pygame coords system.
    vertstart = grid[0]
    vertlinegap = grid[1]
    horigridsize = grid[2]
    horistart = grid[3]
    horilinegap = grid[4]
    vertgridsize = grid[5]

    x = (vertstart + (gridx * vertlinegap)) + (vertlinegap / 2)
    y = ((2 * horistart) + vertgridsize) - (horistart + (gridy * horilinegap)) - (horilinegap / 2)

    return [x, y]


    
