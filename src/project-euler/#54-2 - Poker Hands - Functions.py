cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
ranks = ["High Card",
         "Pair",
         "Two Pairs",
         "Three of a Kind",
         "Straight",
         "Flush",
         "Full House",
         "Four of a Kind",
         "Straight Flush",
         "Royal Flush"]


def cardsort(hand):
    values = [card[0] for card in hand]
    sortedhand = []
    for value in cards:
        for cardi, checkvalue in enumerate(values):
            sortedhand.append(hand[cardi]) if value == checkvalue else None
    return sortedhand


def pair(hand):
    values = [card[0] for card in hand]
    amounts = [values.count(c) for c in cards if c in values]
    return amounts.count(2) == 1


def twopairs(hand):
    values = [card[0] for card in hand]
    amounts = [values.count(c) for c in cards if c in values]
    return amounts.count(2) == 2


def threeofakind(hand):
    values = [card[0] for card in hand]
    amounts = [values.count(c) for c in cards if c in values]
    return 3 in amounts


def straight(hand):
    hand = cardsort(hand)
    values = [card[0] for card in hand]
    return "".join(values) in "".join(cards)


def flush(hand):
    suits = [card[-1] for card in hand]
    return len(set(suits)) == 1


def fullhouse(hand):
    values = [card[0] for card in hand]
    amounts = [values.count(c) for c in cards if c in values]
    amounts.sort()
    return amounts == [2, 3]


def fourofakind(hand):
    values = [card[0] for card in hand]
    amounts = [values.count(c) for c in cards if c in values]
    return max(amounts) >= 4


def straightflush(hand):
    hand = cardsort(hand)
    return ("".join([card[0] for card in hand]) in "".join(cards)) and (len(set([card[-1] for card in hand])) == 1)


def royalflush(hand):
    hand = cardsort(hand)
    return ("".join([card[0] for card in hand]) == "".join(cards[-5:])) and (len(set([card[-1] for card in hand])) == 1)


def getrank(hand):
    if type(hand) == str:
        hand = hand.split()

    if royalflush(hand):
        return "Royal Flush"
    elif straightflush(hand):
        return "Straight Flush"
    elif fourofakind(hand):
        return "Four of a Kind"
    elif fullhouse(hand):
        return "Full House"
    elif flush(hand):
        return "Flush"
    elif straight(hand):
        return "Straight"
    elif threeofakind(hand):
        return "Three of a Kind"
    elif twopairs(hand):
        return "Two Pairs"
    elif pair(hand):
        return "Pair"
    else:
        return "High Card"


def getrelevant(hand, rank):
    if type(hand) == str:
        hand = hand.split()

    if rank == "Royal Flush" or rank == "Straight Flush" or rank == "Full House" or rank == "Straight" or rank == "Flush":
        return [card[0] for card in hand]
    elif rank == "Four of a Kind":
        values = [card[0] for card in hand]
        return [card[0] for card in hand if values.count(card[0]) == 4]
    elif rank == "Three of a Kind":
        values = [card[0] for card in hand]
        return [card[0] for card in hand if values.count(card[0]) == 3]
    elif rank == "Two Pairs" or rank == "Pair":
        values = [card[0] for card in hand]
        return [card[0] for card in hand if values.count(card[0]) == 2]
    else:
        hand = cardsort(hand)
        return [hand[-1]]


def getvalue(hand):
    return sum([cards.index(card[0])+1 for card in hand])
