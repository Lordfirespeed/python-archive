import turtle
from degtrig import *
from time import sleep

boi = turtle.Turtle()
boi.pu()
boi.ht()
boi.pencolor("red")

t = 0
end = 360
incr = 0.5
scale = 10
while t <= end:
    x = scale * (15 * (sin(t) ** 3))
    y = scale * ((13 * cos(t)) - (5 * cos(2 * t)) - (2 * cos(3 * t)) - cos(4 * t))
    boi.goto(x, y)
    boi.pd()
    t += incr
sleep(3)
turtle.bye()
