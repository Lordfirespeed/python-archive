import pygame
import colorsys
import time
rect_x = 50
rect_y = 50
x_increment = 10
y_increment = 10
pygame.init()
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hi")

clock = pygame.time.Clock()

running = True

colours = {"white": (255, 255, 255), "black": (0, 0, 0), "green": (0, 255, 0), "red": (255, 0, 0), "blue": (0, 0, 255)}

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if rect_x < 0 or rect_x > (size[0]-50):
        x_increment = -x_increment
    if rect_y < 0 or rect_y > (size[1]-50):
        y_increment = -y_increment

    rect_x += x_increment
    rect_y += y_increment

    (r, g, b) = colorsys.hsv_to_rgb(float(time.clock() / 10), 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    
    screen.fill(colours["black"]) 

    rectangle = pygame.draw.ellipse(screen, (R, G, B), [rect_x, rect_y, 50, 50], 0)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
