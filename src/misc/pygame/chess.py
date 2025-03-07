import drawgrid
import pygame

size = (700, 500)
displayname = "Chess"
rows, columns = 8, 8

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption(displayname)
clock = pygame.time.Clock()

RUN = True
while RUN:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    GRID = drawgrid.drawsquaregrid(screen, size, rows)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
