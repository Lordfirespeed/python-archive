from math import sqrt


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif type(other) is int:
            return Vector2(self.x + other, self.y + other)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif type(other) is int:
            return Vector2(self.x - other, self.y - other)
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        if type(other) is int:
            return Vector2(self.x * other, self.y * other)
        raise TypeError

    def __repr__(self):
        return f"({self.x}, {self.y})"
