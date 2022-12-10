from math import sqrt
from typing import Union, overload, Self

Number = Union[int, float]


class Vector2:
    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    @classmethod
    def full(cls, value: Number) -> Self:
        return cls(value, value)

    def __abs__(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def __add__(self, other: Self) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        raise TypeError

    def __iadd__(self, other) -> None:
        if isinstance(other, Vector2):
            self.x += other.x
            self.y += other.y
        raise TypeError

    def __sub__(self, other) -> Self:
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        raise TypeError

    def __isub__(self, other) -> None:
        if isinstance(other, Vector2):
            self.x -= other.x
            self.y -= other.y
        raise TypeError

    @overload
    def __mul__(self, other: Self) -> Self: ...

    @overload
    def __mul__(self, other: Number) -> Self: ...

    def __mul__(self, other: Number | Self) -> Self:
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        if isinstance(other, Number):
            return Vector2(self.x * other, self.y * other)
        raise TypeError

    @overload
    def __imul__(self, other: Self) -> None:
        ...

    @overload
    def __imul__(self, other: Number) -> None:
        ...

    def __imul__(self, other: Self | Number) -> None:
        if isinstance(other, Vector2):
            self.x *= other.x
            self.y *= other.y
        if isinstance(other, Number):
            self.x *= other
            self.y *= other
        raise TypeError

    def __hash__(self) -> int:
        # https://stackoverflow.com/a/5929567/11045433
        return (self.x * 73856093) ^ (self.y * 83492791)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
