from math import sqrt

class Vec2():
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, __x):
        x = self.x + __x.x
        y = self.y + __x.y
        return Vec2(x, y)

    def __sub__(self, __x):
        x = self.x - __x.x
        y = self.y - __x.y
        return Vec2(x, y)

    def __mul__(self, __x):
        x = self.x * __x
        y = self.y * __x
        return Vec2(x, y)

    def __div__(self, __x):
        x = self.x / __x
        y = self.y / __x
        return Vec2(x, y)
    
    def __rdiv__(self, __x):
        x = self.x / __x
        y = self.y / __x
        return Vec2(x, y)

    def __str__(self) -> str:
        return f"({self.x} , {self.y})"

    def normalize(self):
        length = sqrt(self.x**2 + self.y**2)
        if length != 0:
            return Vec2(self.x / length, self.y / length)
        return self

    @property
    def ZERO():
        return Vec2(0, 0)

    @property
    def RIGHT():
        return Vec2(1, 0)

    @property
    def UP():
        return Vec2(0, 1)
