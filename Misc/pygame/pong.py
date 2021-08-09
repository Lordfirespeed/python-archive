import pygame
import colorsys
import time

size = (700, 500)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

leftplayerx = size[0] / 15
leftplayery = size[1] / 2

rightplayerx = size[0] - (leftplayerx)
rightplayery = leftplayery

playerheight = 50
playerwidth = 5
playerspeed = 5
movedict = {"up": (-1 * playerspeed), "down": (playerspeed), "none": 0}

leftplayermove = "none"
rightplayermove = "none"

ballsize = min(size) / 25

ballx = (size[0] / 2) - (ballsize / 2)
bally = (size[1] / 2) - (ballsize / 2)

ballspeed = 4
ballxinc = ballspeed
ballyinc = ballspeed
hitplayer = False
ballrect = pygame.Rect(ballx, bally, ballsize, ballsize)

running = True
while running:

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keyname = pygame.key.name(event.key)
            if keyname == "w":
                leftplayermove = "up"
            elif keyname == "up":
                rightplayermove = "up"
            elif keyname == "s":
                leftplayermove = "down"
            elif keyname == "down":
                rightplayermove = "down"
            
        elif event.type == pygame.KEYUP:
            keyname = pygame.key.name(event.key)
            if keyname == "w":
                leftplayermove = "none"
            elif keyname == "up":
                rightplayermove = "none"
            elif keyname == "s":
                leftplayermove = "none"
            elif keyname == "down":
                rightplayermove = "none"

    #COMPARISON AND LOGIC
    if leftplayermove != "none":
        leftplayery += movedict[leftplayermove]
        if leftplayery > (size[1] - playerheight):
            leftplayery = (size[1] - playerheight)
        elif leftplayery < 0:
            leftplayery = 0

    if rightplayermove != "none":
        rightplayery += movedict[rightplayermove]
        if rightplayery > (size[1] - playerheight):
            rightplayery = (size[1] - playerheight)
        elif rightplayery < 0:
            rightplayery = 0

    leftplayer = pygame.Rect(leftplayerx, leftplayery, playerwidth, playerheight)
    rightplayer = pygame.Rect(rightplayerx, rightplayery, playerwidth, playerheight)

    if bally < 0 or bally > (size[1] - ballsize):
        ballyinc = -1 * ballyinc

    if not hitplayer:
        if ballrect.colliderect(leftplayer) or ballrect.colliderect(rightplayer):
            ballxinc = -1 * ballxinc
            hitplayer = True
    else:
        if (not ballrect.colliderect(leftplayer)) and (not ballrect.colliderect(rightplayer)):
            hitplayer = False

    ballx += ballxinc
    bally += ballyinc
            
    ballrect = pygame.Rect(ballx, bally, ballsize, ballsize)

    ballspeed += 0.1

    #DRAWING
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), leftplayer)
    pygame.draw.rect(screen, (255, 255, 255), rightplayer)
    pygame.draw.ellipse(screen, (255, 255, 255), ballrect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
