from itertools import permutations
from math import comb

socks = ["Y", "O", "P", "W"]
shoes = ["B", "R", "G"]
foot = ["L", "L", "R", "R"]

valid_foot_orders = []
for foot_order in permutations(foot):
    if foot_order.count("L") == 2 and foot_order.count("R") == 2 and foot_order not in valid_foot_orders:
        valid_foot_orders.append(foot_order)  # get all the (6) orders in which feet can be chosen

sock_choices = comb(4, 2)  # 4C2 = 6
sock_arrangements = sock_choices * 2  # as socks can be 'reversed'; swap the foot they are put onto (12)

shoe_choices = len(shoes)  # shoes must match

print(sock_arrangements * shoe_choices * len(valid_foot_orders))  # 216
