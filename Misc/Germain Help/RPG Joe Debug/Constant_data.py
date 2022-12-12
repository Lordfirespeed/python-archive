# Player Input
player_combat_action = {"attack": 1, "a": 1, "defend": 2, "d": 2, "magic": 3, "m": 3}
player_magic_action = {"heal": 1, "h": 1, "missile": 2, "m": 2, "cancel": 3, "c": 3}

# Responses to player
magic_list = ["\nHeal Light Wounds (+10 HP, -5 Mana)", "\nMelf's Magic Missile (20 point unmissable damage, -10 Mana)"]
responses = {"insuf_m": "\nInsufficient Mana",
             "game_over": "\nThe light fades to black. You lose feeling.\nGame Over",
             "combat_option": "\nWould you like to: Attack, Defend or use Magic?",
             "invalid": "\nInvalid input, please use something different",
             "can": "\nCancel"}

# Player Variables
player_alive = True
player_attack = False
player_defend = False
player_magic = False
player_variables = []

# Enemy Variables
enemy_health = 0
c = 0

# Entities (characters)
player = {"s": 10, "d": 15, "hp": 30, "m": 10, "w": 2, "unique": 0}
goblin = {"s": 5, "d": 10, "hp": 10, "w": 1, "g": 5, "e": 10, "unique": 1}
orc = {"s": 13, "d": 13, "hp": 15, "w": 2, "g": 10, "e": 15, "unique": 2}
earth_elemental = {"s": 16, "d": 16, "hp": 5, "w": 3, "g": 0, "e": 30, "unique": 3}
djinn = {"s": 5, "d": 16, "hp": 10, "w": 4, "g": 30, "e": 15, "c": 17, "unique": 4}
dragon = {"s": 18, "d": 18, "hp": 30, "w": 5, "g": 100000000, "e": 500, "unique": 5}
entity_list = [player, goblin, orc, earth_elemental, djinn, dragon]
entity_name_list = ["Player", "Goblin", "Orc", "Earth Elemental", "Djinn", "Dragon"]

# Entities (Items)
weapons_names = {1: "dagger", 2: "sword", 3: "rock fist", 4: "harsh language", 5: "fire breath"}
weapons = {1: [3, 1, 0], 2: [6, 1, 0], 3: [8, 1, 3], 4: [4, 1, c], 5: [12, 2, 0]}

# Entities (Magic)
magic_names = {1: "Cure Light Wounds", 2: "Melf's Magic Missile"}
magic_values = {1: [5, 10, 0], 2: [10, 0, 20]}

