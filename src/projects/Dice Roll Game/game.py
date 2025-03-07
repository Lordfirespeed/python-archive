import sqlite3
import random

loggedInA = None
loggedInB = None

conn = sqlite3.connect("database.db")
db = conn.cursor()

import usersystem


def dice():
    return random.randrange(1, 6)


def specialcases(scores):
    if sum(scores) % 2 == 0:
        print("+10 SCORE! Even number.")
        scores.append(10)
    else:
        print("-5 SCORE! Odd number.")
        scores.append(-5)

    if scores[0] == scores[1]:
        input("DOUBLE! Roll one extra dice...")
        scores.append(dice())
        print("You rolled: %d" % scores[-1])

    return scores


def playerturn(player):
    scores = []
    input("%s's Roll..." % player)
    scores += [dice(), dice()]
    print("You rolled: %d, %d" % (scores[0], scores[1]))
    scores = specialcases(scores)
    print("%s's score for this round: %d" % (player, sum(scores)))

    return sum(scores)


def gameround(players=["Player A", "Player B"]):
    scoreA = playerturn(players[0])
    scoreB = playerturn(players[1])
    return scoreA, scoreB


def playgame():
    global loggedInA
    global loggedInB

    if (not loggedInA) and (not loggedInB):
        print("No users are logged in. Two people need to log in to play.")
        return None
    elif not loggedInA:
        print("User A is not logged in. Two people need to be logged in to play.")
        return None
    elif not loggedInB:
        print("User B is not logged in. Two people need to be logged in to play.")
        return None

    usernameA = usersystem.getuser("ID", loggedInA)[1]
    usernameB = usersystem.getuser("ID", loggedInB)[1]
    playerNames = [usernameA, usernameB]
    scoreA, scoreB = 0, 0

    for roundNum in range(1, 6):
        print("ROUND %d" % roundNum)
        roundScores = gameround(playerNames)
        scoreA += roundScores[0]
        scoreA = 0 if scoreA < 0 else scoreA
        scoreB += roundScores[1]
        scoreB = 0 if scoreB < 0 else scoreB
        if roundNum != 5:
            if scoreA == scoreB:
                print("%s and %s are tied with %d points." % (usernameA, usernameB, scoreA))
            else:
                winning = usernameA if scoreA > scoreB else usernameB
                losing = (set(playerNames) - {winning}).pop()
                print("%s is winning with %d points." % (winning, max([scoreA, scoreB])))
                print("%s is behind with %d points." % (losing, min([scoreA, scoreB])))
        print()

    while scoreA == scoreB:
        print("ROLL-OFF! Players are tied!")
        input("%s's roll..." % usernameA)
        scoreA = dice()
        print("You rolled: %d" % scoreA)
        input("%s's roll..." % usernameB)
        scoreB = dice()
        print("You rolled: %d" % scoreB)

    winner = usernameA if scoreA >= scoreB else usernameB
    loser = (set(playerNames) - {winner}).pop()

    print("GAME OVER!")
    print("%s won with a total of %d points." % (winner, max([scoreA, scoreB])))
    print("%s lost, with only %d points. Oh dear!" % (loser, min([scoreA, scoreB])))

    winnerID = int(loggedInA) if winner == usernameA else int(loggedInB)
    loserID = ({loggedInA, loggedInB} - {winnerID}).pop()

    winnerFileName = usersystem.userDirectory + str(winnerID) + "-" + winner + ".txt"
    loserFileName = usersystem.userDirectory + str(loserID) + "-" + loser + ".txt"

    with open(winnerFileName, "a") as winnerFile:
        winnerFile.write(str(max([scoreA, scoreB])) + "W [" + usersystem.gettimenow() + "]\n")

    with open(loserFileName, "a") as loserFile:
        loserFile.write(str(min([scoreA, scoreB])) + "L [" + usersystem.gettimenow() + "]\n")


def gethelp():
    global validCommands
    print("Valid commands:\n- " + "\n- ".join(validCommands))


def exitgame():
    print("Thank you for beta-testing Joe's Dice Roll Game.")
    exit(0)


validCommands = {"login": "usersystem.",
                 "createuser": "usersystem.",
                 "playgame": "",
                 "playerstats": "usersystem.",
                 "leaderboard": "usersystem.",
                 "gethelp": "",
                 "exitgame": ""}

execCommands = None
mainloop = True
while mainloop:
    usersystem.loggedInA = loggedInA
    usersystem.loggedInB = loggedInB
    userinput = usersystem.validentry(list(validCommands), "command")
    exec("execCommands = " + validCommands[userinput] + userinput + "()", globals(), locals())
    if execCommands:
        [exec(cmd, globals()) for cmd in execCommands]
        execCommands = None
