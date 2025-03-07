import random
import Constant_data
import sys


def combat(opponent):
    global enemy, enemy_health, player_alive, player_variables
    enemy = Constant_data.entity_list[opponent]
    enemy_health = enemy["hp"]
    enemy_alive = True

    print("\nYou've ran into a %s, ready yourself" % (Constant_data.entity_name_list[enemy["unique"]]))

    while enemy_alive and player_alive:
        player_turn()
        enemy_turn()

        print("\n%s has %d health" % (Constant_data.entity_name_list[opponent], enemy_health))
        player_alive = alive_check(player_variables[0])
        enemy_alive = alive_check(enemy_health)

    if player_alive:
        print("\nYou have slain %s" % (Constant_data.entity_name_list[enemy["unique"]]))
        player_variables[2] += enemy["g"]
        player_variables[3] += enemy["e"]
        print("\nYou have earned %d gold and %d exp" % (enemy["g"], enemy["e"]),
              "\nIn the conclusion of the battle you are left with HP: %d/%d, Mana: %d/%d" % (
                  player_variables[0], Constant_data.player["hp"], player_variables[1], Constant_data.player["m"]))
    else:
        print(Constant_data.responses["game_over"])
        sys.exit()


def player_turn():
    global player_variables
    print("\nHP: %d/%d, Mana: %d/%d, Strength: %d, Dexterity: %d" % (
        player_variables[0], Constant_data.player["hp"], player_variables[1], Constant_data.player["m"], Constant_data.player["s"], Constant_data.player["d"]))
    action = False
    while not action:
        action = combat_application()


def combat_application():
    global player_defend, player_variables

    while True:
        print(Constant_data.responses["combat_option"])
        answer = input("\n").lower()

        if answer in Constant_data.player_combat_action.keys():
            answer = Constant_data.player_combat_action[answer]
            break
        else:
            print(Constant_data.responses["invalid"])
            continue

    player_defend = False

    if answer == 1:
        print("\nYou choose to attack", Constant_data.entity_name_list[enemy["unique"]])
        attack(Constant_data.player, enemy)
        return True
    elif answer == 2:
        print(
            "\nYou decide to defend yourself decreasing your chance of your opponent landing a strike while conserving own your energy")
        player_defend = True
        mana_modify(1)
        return True
    elif answer == 3:
        return magic()


# Attack functions
def attack(who, what):
    global enemy_health, player_variables

    hit = hit_check(who)
    hurt = damage(*weapons[who["w"]])

    if not hit:
        print("\n%s: missed %s" % (Constant_data.entity_name_list[who["unique"]], Constant_data.entity_name_list[what["unique"]]))
    elif who["unique"] == 0:
        enemy_health -= hurt
        print("\n%s: Hit %s for %d damage" % (
        Constant_data.entity_name_list[who["unique"]], Constant_data.entity_name_list[what["unique"]], hurt))
    elif not who["unique"] == 0:
        player_variables[0] -= hurt
        print("\n%s: Hit %s for %d damage" % (
        Constant_data.entity_name_list[who["unique"]], Constant_data.entity_name_list[what["unique"]], hurt))


def hit_check(who):
    d20 = random.randint(1, 20)
    attempt = d20 + who["s"]

    if who["unique"] == 0:
        if d20 == 20:
            return True
        elif d20 == 1:
            return False
        elif attempt > enemy["d"]:
            return True
        else:
            return False

    elif not who["unique"] == 0:
        if d20 == 20:
            return True
        elif d20 == 1:
            return False
        elif attempt > 2 * Constant_data.player["d"]:
            return True
        elif not player_defend and attempt > Constant_data.player["d"]:
            return True
        else:
            return False


def damage(value_of_dice, number_of_dice, additional_damage):
    hurt_points = []

    for Number_of_Dice in range(number_of_dice):
        hurt_points.append(random.randint(1, value_of_dice))
    hurt_points.append(additional_damage)
    hurt_points = sum(hurt_points)
    return hurt_points


# Magic functions
def magic():
    global enemy_health, player_variables, respond
    respond = []
    while True:
        print("\nWhich magic would you like to use?", *Constant_data.magic_list, "\nor cancel\n")
        answer = input().lower()

        if answer in Constant_data.player_magic_action:
            answer = Constant_data.player_magic_action[answer]
            break
        else:
            print(Constant_data.responses["invalid"])
            continue

    if answer == 3:
        print(Constant_data.responses["can"])
        return False
    elif player_variables[1] >= Constant_data.magic_values[answer][0]:
        player_variables[1] -= Constant_data.magic_values[answer][0]
        respond = ["\n-%d Mana Points" % (Constant_data.magic_values[answer][0])]
        health_modify(Constant_data.magic_values[answer][1])
        enemy_health_modify(Constant_data.magic_values[answer][2])
        print(*respond)
        return True
    else:
        print(Constant_data.responses["insuf_m"])
        return False


# Enemy functions
def enemy_turn():
    global c, weapons
    if "c" in enemy:
        weapons[4][2] = enemy["c"]
    else:
        weapons[4][2] = 0
    attack(enemy, Constant_data.player)


# Modify value functions (the functions only work for positive increases)
def health_modify(amount):
    global player_variables, respond
    if amount == 0:
        pass
    elif player_variables[0] + amount > Constant_data.player["hp"]:
        respond.append("\n%d Damage healed (limited by maximum health)" % (
                    Constant_data.player["hp"] - player_variables[0]))
        player_variables[0] = Constant_data.player["hp"]
    else:
        respond.append("\n%d Damage healed" % amount)
        player_variables[0] += amount


def enemy_health_modify(amount):
    global respond, enemy_health
    if amount == 0:
        pass
    else:
        respond.append("\n%d Points of damage dealt to %s" % (amount, Constant_data.entity_name_list[enemy["unique"]]))
        enemy_health -= amount


def mana_modify(amount):
    global player_variables

    if amount == 0:
        pass
    elif player_variables[1] + amount >= Constant_data.player["m"]:
        print("\nMana +%d (limited by maximum mana)" % (Constant_data.player["m"] - player_variables[1]))
        player_variables[1] = Constant_data.player["m"]
    else:
        print("\nMana +%d" % amount)
        player_variables[1] += amount


# State checks
def alive_check(check):
    if check < 1:
        return False
    else:
        return True
