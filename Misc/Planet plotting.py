import turtle
import math

screen = turtle.Screen()


def degsin(x):
    return math.sin(math.radians(x))


def degcos(x):
    return math.cos(math.radians(x))


def degtan(x):
    return math.tan(math.radians(x))


def l2int(iterobj):
    return tuple([int(x) for x in iterobj])


def makeplanetobj(shape, size, color):
    planet = turtle.RawTurtle(screen)
    planet.ht()
    planet.speed(10)
    planet.shape(name=shape)
    planet.shapesize(size)
    planet.color(color)
    planet.pu()
    planet.st()
    return planet


def newdrawpoint():
    drawpoint = turtle.RawPen(screen)
    drawpoint.ht()
    drawpoint.speed(10)
    return drawpoint


def getplanetpos(orbitsize, angle):
    yval = degsin(angle) * orbitsize
    xval = degcos(angle) * orbitsize
    return xval, yval


sun = makeplanetobj("circle", 1, "yellow")
planetA = makeplanetobj("circle", 0.5, "blue")
planetB = makeplanetobj("circle", 0.3, "lime")
drawpointA = newdrawpoint()
drawpointA.color("grey")
drawpointA.pu()


def plot(orbitSizeA=300, orbitSpeedA=1, orbitSizeB=195, orbitSpeedB=1.3, colour="grey"):
    drawpointA.pencolor(colour)
    currAngleA = 0
    currAngleB = 0

    planetA.setposition(orbitSizeA, 0)
    planetB.setposition(orbitSizeB, 0)

    done = False
    while not done:
        planetA.goto(getplanetpos(orbitSizeA, currAngleA))
        planetB.goto(getplanetpos(orbitSizeB, currAngleB))
        drawpointA.setposition(planetA.pos())
        drawpointA.pd()
        drawpointA.goto(planetB.pos())
        drawpointA.pu()
        sun.forward(0)
        currAngleA += 10 * orbitSpeedA
        currAngleB += 10 * orbitSpeedB
        done = (currAngleA % 360, currAngleB % 360) == (0, 0)

    planetA.goto(orbitSizeA, 0)
    planetB.setposition(orbitSizeB, 0)
