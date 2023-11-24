from tito_engine import *
from custom_objs import *

player = TopDownCharacterController(
    3.0, path_to_img='assets/sprites/Survivor 1/survivor1_gun.png',
    transform=Transform(Vec2(30, 360)),
    tag='Player'
)

zombie1 = Zombie(2.0, 20.0, 200.0, 'assets/sprites/Zombie 1/zoimbie1_hold.png',
                 Transform(Vec2(540, 360)))

TitoEngine(colour_fill=(40, 40, 40)).run([player, zombie1])
