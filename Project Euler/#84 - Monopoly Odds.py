from fractions import Fraction

board = "GO,A1,CC1,A2,T1,R1,B1,CH1,B2,B3,JAIL,C1,U1,C2,C3,R2,D1,CC2,D2,D3,FP,E1,CH2,E2,E3,R3,F1,F2,U2,F3,G2J,G1,G2,CC3,G3,R4,CH3,H1,T2,H2".split(",")
boardsize = len(board)
initchance = Fraction(1, boardsize)
piecetypeboard = [p[:-1] for p in board]
commchest, chance = 16, 16

dicesides = 6
doublechance = Fraction(1, dicesides)
threeconsecdoublechance = doublechance ** 3
jailinitchance = initchance + threeconsecdoublechance
otherinitchance = (1 - jailinitchance) / (boardsize - 1)
chances = dict(zip(board, [otherinitchance for _ in range(boardsize)]))
chances["JAIL"] = jailinitchance

for place in board:
    if place[:-1] == "CC":
        changechance = chances[place] * Fraction(1, commchest)
        chances["GO"] += changechance
        chances["JAIL"] += changechance
        chances[place] -= 2 * changechance
    elif place[:-1] == "CH":
        changechance = chances[place] * Fraction(1, chance)
        chances["GO"] += changechance
        chances["JAIL"] += changechance
        chances["C1"] += changechance
        chances["E3"] += changechance
        chances["H2"] += changechance
        chances["R1"] += changechance
        nextR = board[(2 * piecetypeboard).index("R", board.index(place)) % boardsize]
        nextU = board[(2 * piecetypeboard).index("U", board.index(place)) % boardsize]
        back3 = (2 * board)[board.index(place) + boardsize - 3]
        chances[nextR] += 2 * changechance
        chances[nextU] += changechance
        chances[back3] += changechance
        chances[place] -= 10 * changechance
    elif place == "G2J":
        chances["JAIL"] += chances[place]
        chances[place] = 0

backwardschances = list(zip(chances.values(), chances.keys()))
modalstring = ""
for top in range(3):
    maxchance = max(backwardschances)
    placestring = str(board.index(maxchance[1]))
    placestring = "0" * (2 - len(placestring)) + placestring
    modalstring += placestring
    backwardschances.remove(maxchance)
print(modalstring)
