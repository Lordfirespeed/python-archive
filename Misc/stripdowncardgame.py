from random import randrange

def shuffle(cards):
    unshuffled = cards.copy()
    shuffled = list()
    while unshuffled != []:
        index = randrange(0, len(unshuffled))
        shuffled.append(unshuffled[index]))
        del unshuffled[index]
    return shuffled

print("pre-init...")

players = 6
cardnums = ["A"] + [str(c) for c in list(range(2,10))] + ["J", "Q", "K"]
cardsuits = ["S", "C", "D", "H"]
cards = [num+suit for num in cardnums for suit in cardsuits]

print("init...")
print(shuffle(cards))