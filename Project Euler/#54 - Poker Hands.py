pfunc = __import__("#54-2 - Poker Hands - Functions")

with open("#52-poker.txt") as inputfile:
    inputlines = [line.strip() for line in inputfile.readlines()]

inputdata = [[line.split()[:5], line.split()[5:]] for line in inputlines]
winners = []
noneasy = []
recordranks = []

for gindex, game in enumerate(inputdata, 1):
    winner = 0
    playera = game[0]
    playerb = game[1]
    ranka = pfunc.getrank(playera)
    rankb = pfunc.getrank(playerb)
    recordranks.append([ranka, rankb])
    if ranka != rankb:
        winner = 1 if pfunc.ranks.index(ranka) > pfunc.ranks.index(rankb) else 2
    else:
        playera = pfunc.cardsort(playera)
        playerb = pfunc.cardsort(playerb)
        valuesa = [card[0] for card in playera]
        valuesb = [card[0] for card in playerb]

        relevanta = pfunc.getrelevant(playera, ranka)
        relevantb = pfunc.getrelevant(playerb, rankb)
        relevanta.sort()
        relevantb.sort()
        totvaluea = pfunc.getvalue(relevanta)
        totvalueb = pfunc.getvalue(relevantb)

        if totvaluea != totvalueb and relevanta != relevantb:
            winner = 1 if totvaluea > totvalueb else 2
        else:
            for cardi in range(4, -1, -1):
                cardranka = pfunc.cards.index(playera[cardi][0])
                cardrankb = pfunc.cards.index(playerb[cardi][0])
                if cardranka != cardrankb:
                    winner = 1 if cardranka > cardrankb else 2
                    break

    winners.append(winner)

print("Player 1 wins %s times out of the %s examples in the file." % (winners.count(1), len(inputdata)))

# wrong = []
# for index in range(len(inputdata)):
#     print("\nGame %s" % index)
#     print("Player 1: %s, %s" % (" ".join(inputdata[index][0]), recordranks[index][0]))
#     print("Player 2: %s, %s" % (" ".join(inputdata[index][1]), recordranks[index][1]))
#     print("Player %s won." % winners[index])
#     userinput = input("> ")
#     wrong.append(index) if userinput == "n" else None
