from tito_engine import *
import pygame as pg


class TopDownController(Sprite):
    def __init__(self, move_speed: float, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self.move_speed = move_speed
        super().__init__(path_to_img, transform, enabled)

    def update(self, world):
        self.move()
        super().update(world)

    def move(self):
        y_input = InputManager.get_axis(pg.K_w, pg.K_s)
        x_input = InputManager.get_axis(pg.K_a, pg.K_d)

        self.transform.position += Vec2(x_input, y_input) * self.move_speed


player = PhysicSprite(
    gravity=0.01,
    path_to_img='assets/sprites/knight.png',
    transform=Transform(Vec2(540, 360), 0, 1.25),
    tag='Player'
)

TitoEngine().run([player])
