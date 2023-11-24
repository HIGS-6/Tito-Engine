from tito_engine import Sprite, Transform, InputManager, Vec2
import pygame as pg


class TopDownCharacterController(Sprite):
    def __init__(self, move_speed: float, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self._move_speed = move_speed
        super().__init__(path_to_img, transform, enabled, tag)

    def update(self, world):
        self.look()
        self.move()
        super().update(world)

    def move(self):
        # Get the input from WSAD Keys, make a vector from them and update the objects's position
        x_input, y_input = InputManager.get_axis(
            pg.K_a, pg.K_d), InputManager.get_axis(pg.K_w, pg.K_s)

        self.transform.position += Vec2(x_input,
                                        y_input).normalize() * self._move_speed

    def look(self):
        # Rotate the sprite to look at the mouse position at all times
        mouse_pos = InputManager.get_mouse_pos()
        self.transform.look_at(mouse_pos)
