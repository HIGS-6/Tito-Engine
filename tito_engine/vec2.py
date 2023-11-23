class Vec2:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, __x):
        x = self.x + __x.x
        y = self.y + __x.y
        return Vec2(x, y)

    def __mul__(self, __x):
        x = self.x * __x
        y = self.y * __x
        return Vec2(x, y)

    def __div__(self, __x):
        x = self.x / __x
        y = self.y / __x
        return Vec2(x, y)

    def __str__(self) -> str:
        return f"({self.x} , {self.y})"

    @property
    def ZERO():
        return Vec2(0, 0)

    @property
    def RIGHT():
        return Vec2(1, 0)

    @property
    def UP():
        return Vec2(0, 1)
