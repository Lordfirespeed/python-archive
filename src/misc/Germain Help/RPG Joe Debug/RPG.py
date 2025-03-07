import random
import Combat
import Constant_data

while Constant_data.player_alive:
    Combat.combat(random.randint(1, 5))
