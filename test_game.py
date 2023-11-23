from tito_engine import *
from custom_objs import *

player = TopDownCharacterController(
    3.0, path_to_img='assets/sprites/survivor-idle_knife_0.png',
    transform=Transform(Vec2(540, 360), 0.0, 0.5),
    tag='Player'
)

TitoEngine().run([player])
