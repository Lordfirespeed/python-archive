from random import randrange
from string import ascii_letters as alphabet

players = 6
playernames = [alphabet[i] for i in range(players)]


def removeplayer(playerindex):
    global players
    global playercards
    global playernames

    del playercards[playerindex]
    del playernames[playerindex]
    players -= 1


def shuffle(cards):
    unshuffled = cards.copy()
    shuffled = list()
    while unshuffled != []:
        index = randrange(0, len(unshuffled))
        shuffled.append(unshuffled[index])
        del unshuffled[index]
    return shuffled


cardnums = ["A"] + [str(c) for c in list(range(2, 10))] + ["J", "Q", "K"]
cardsuits = ["S", "C", "D", "H"]
cards = [num + suit for num in cardnums for suit in cardsuits]
cards += ["Jk", "Jk"]

deck = shuffle(cards)
playercards = [[] for i in range(players)]
[playercards[i % players].append(card) for i, card in enumerate(deck)]  # this deals the cards

valdict = {"J": 1, "Q": 2, "K": 3, "A": 4, "Jk": 5}
currplayer = 0
discard = []
while len(playercards) != 1:
    checkprev = False
    if len(discard) > 0:
        checkprev = True
        prev = discard[-1]

    if checkprev and prev[0] in ["A", "J", "Q", "K"]:
        if prev == "Jk":
            tries = 5
        else:
            tries = valdict[prev[0]]

        removedPlayer = False
        failed = True
        for attempt in range(tries):
            discard.append(playercards[currplayer].pop(0))
            if discard[-1][0] in ["A", "J", "Q", "K"]:
                failed = False
                break
            if not playercards[currplayer]:
                removeplayer(currplayer)
                break

        if failed:
            currplayer -= 1
            playercards[currplayer] += discard.copy()
            discard = []

    else:
        discard.append(playercards[currplayer].pop(0))

    if not playercards[currplayer]:
        removeplayer(currplayer)
    else:
        currplayer += 1

    currplayer %= players
    print(playercards, "Discard", discard, "Player", currplayer)

print(playernames[0])
