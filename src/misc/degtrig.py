from math import cos as radcos, sin as radsin, radians as torad


def sin(x):
    return radsin(torad(x))


def cos(x):
    return radcos(torad(x))
