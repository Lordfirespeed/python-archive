import random
from sys import stdout
from time import sleep


def bool_percent(percent_chance):
    true_list = [True for onepercent in range(percent_chance)]
    false_list = [False for onepercent in range((100 - percent_chance))]
    pick_list = true_list + false_list
    return random.choice(pick_list)


def write(string, speed=20):
    for character in string:
        stdout.write(character)
        sleep(1/speed)
    stdout.write("\n")

