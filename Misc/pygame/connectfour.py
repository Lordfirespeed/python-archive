import pygame
from connectfourwin import checkwin
import drawgrid
from time import sleep

size = (1000, 700)
columns = 9
rows = 8

global GRID
global vertstart
global vertlinegap
global horistart
global horilinegap
vertstart = size[0] / 14
vertlinegap = (size[0] - (vertstart * 2)) / columns
horistart = size[1] / 20
horilinegap = (size[1] - (horistart * 2)) / rows

def drawcounter(row, column, colour):
    global size
    global vertstart
    global vertlinegap
    global horistart
    global horilinegap

    countersize = min(vertlinegap, horilinegap) * 0.9

    x = (vertstart + (column * vertlinegap)) + ((vertlinegap / 2) - (countersize / 2))
    y = (size[1] - (horistart + (row * horilinegap)) - horilinegap) + ((horilinegap / 2) - (countersize / 2))
    pygame.draw.ellipse(screen, colour, (x, y, countersize, countersize), 0)

def drawwinline(startcounter, endcounter):
    global size
    global vertstart
    global vertlinegap
    global horistart
    global horilinegap
    global GRID

    startx, starty = drawgrid.coordsgrid(GRID, startcounter[0], startcounter[1])
    endx, endy = drawgrid.coordsgrid(GRID, endcounter[0], endcounter[1])
    
    pygame.draw.line(screen, GREEN, (startx, starty), (endx, endy), 5)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

colourdict = {"BLUE": (0, 0, 255), "RED": (255, 0, 0)}

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

columnlist = [[] for column in range(columns)]
topofgrid = size[1] / 20
bottomofgrid = size[1] - (topofgrid)
columnrectlist = []
for column in range(columns):
    rect_x = vertstart + (vertlinegap * column)
    command = ("columnrect" + str(column) + " = pygame.Rect(" + str(rect_x) + ", " + str(topofgrid) +", " + str(vertlinegap) + ", " + str(bottomofgrid) + ")")
    exec(command)
    exec("columnrectlist.append(columnrect" + str(column) + ")")

switchturn = {"RED": "BLUE", "BLUE": "RED"}

colourturn = "BLUE"
running = True
while running:

    rectnum = -1
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for rectangle in columnrectlist:
                if rectangle.collidepoint(pos):
                    columnnum = round((rectangle[0] - 50) / vertlinegap)
                    if len(columnlist[columnnum]) < rows:
                        columnlist[columnnum].append(colourturn)
                        colourturn = switchturn[colourturn]
                           
    #calculations
    wincheck = (checkwin(columnlist, columns, rows))

    screen.fill(BLACK)
    # drawing
    GRID = drawgrid.drawgrid(screen, size, rows, columns)

    for columnindex, COLUMN in enumerate(columnlist, 0):
        for rowindex, ROW in enumerate(COLUMN, 0):
            drawcounter(rowindex, columnindex, colourdict[ROW])

    if wincheck[0]:
        drawwinline(wincheck[1][0], wincheck[1][3])
        running = False
        pygame.display.flip()
        sleep(5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
