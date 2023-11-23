from math import cos, sin, radians
from .vec2 import Vec2


class Transform:
    """
    # Transform Class
    holds the objects's:
    - Position (Vector2, X and Y)
    - Rotation in degrees (float 0 - 360)
    - Scale (Not-Negative float)
    """

    def __init__(self, position=Vec2(), rotation=0.0, scale=1.0) -> None:
        self._position = position
        self._rotation = rotation
        self._scale = scale

    @property
    def position(self) -> Vec2:
        """The position."""
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def rotation(self) -> float:
        """The rotation."""
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        if value >= 360:
            self._rotation = value - 360
        elif value < 0:
            self._rotation = value + 360
        else:
            self._rotation = value

    @property
    def scale(self) -> float:
        """The scale."""
        return self._scale

    @scale.setter
    def scale(self, value):
        if value < 0:
            raise ValueError(
                'Scale of an object can\'t be negative, you dumb s****')
        self._scale = value

    def translate(self, new_pos: Vec2):
        self._position += new_pos

    def forward(self) -> Vec2:
        frw_vec = Vec2.ZERO

        frw_vec.x = round(sin(radians(self._rotation)), 2)
        frw_vec.y = round(cos(radians(self._rotation)), 2)

        return frw_vec
