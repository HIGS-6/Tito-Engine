from tito_engine import Sprite, Transform, InputManager, Vec2
from math import atan2, degrees
import pygame as pg


class TopDownCharacterController(Sprite):
    def __init__(self, move_speed: float, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self._move_speed = move_speed
        super().__init__(path_to_img, transform, enabled, tag)

    def update(self, world):
        self.face_mouse_pos()
        self.move()
        super().update(world)

    def move(self):
        # Get the input from WSAD Keys, make a vector from them and update the objects's position
        x_input, y_input = InputManager.get_axis(
            pg.K_a, pg.K_d), InputManager.get_axis(pg.K_w, pg.K_s)

        self.transform.position += Vec2(x_input,
                                        y_input).normalize() * self._move_speed

    def face_mouse_pos(self):
        # Calculate the look angle and rotate the sprite
        mouse_pos = InputManager.get_mouse_pos()

        rel_x, rel_y = mouse_pos.x - \
            self.transform.position.x, mouse_pos.y - self.transform.position.y

        angle = degrees(-atan2(rel_y, rel_x))

        self.transform.rotation = int(angle)
