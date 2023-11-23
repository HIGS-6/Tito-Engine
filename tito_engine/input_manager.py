from pygame import key, mouse, event, KEYDOWN
from .vec2 import Vec2


class InputManager:
    """Manages the game input."""

    @staticmethod
    def get_mouse_button(btn: int) -> bool:
        """
        * Left Mouse Button: 0
        * Right Mouse Button: 1
        * Middle Mouse Button: 2
        """
        pressed_keys = mouse.get_pressed()

        return bool(pressed_keys[btn])

    @staticmethod
    def get_key_down(key: key) -> bool:
        for ev in event.get():
            if ev.type == KEYDOWN:
                return ev.key == key

    @staticmethod
    def get_key(key: key) -> bool:
        pressed_keys = key.get_pressed()

        return bool(pressed_keys[key])

    @staticmethod
    def get_axis(pos_value: key, neg_value: key) -> int:
        pressed_keys = key.get_pressed()

        val = 0

        if pressed_keys[pos_value]:
            val -= 1
        if pressed_keys[neg_value]:
            val += 1

        return val

    @staticmethod
    def get_mouse_pos() -> Vec2:
        return Vec2(mouse.get_pos()[0], mouse.get_pos()[1])
