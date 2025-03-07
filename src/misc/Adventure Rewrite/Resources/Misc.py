import random


def boolprob(chance, outof):
    true_list = [True for onepercent in range(chance)]
    false_list = [False for onepercent in range(chance, outof)]
    pick_list = true_list + false_list
    return random.choice(pick_list)

