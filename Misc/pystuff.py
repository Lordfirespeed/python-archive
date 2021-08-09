import pygame
rect_x = 50
rect_y = 50
x_increment = 3
y_increment = 3
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hi")

clock = pygame.time.Clock()

running = True

colours = {"white": (255, 255, 255), "black": (0, 0, 0), "green": (0, 255, 0), "red": (255, 0, 0), "blue": (0, 0, 255)}

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if rect_x < 0 or rect_x > 650:
        x_increment = -x_increment
    if rect_y < 0 or rect_y > 450:
        y_increment = -y_increment

    rect_x += x_increment
    rect_y += y_increment
    
    screen.fill(colours["black"]) 

    rectangle = pygame.draw.ellipse(screen, colours["white"], [rect_x, rect_y, 50, 50], 0)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
