import re
import os
from __main__ import *

userFilePattern = re.compile("[1-9]*-.*\.txt")  # matches '1-Lordfirespeed.txt' and '14-Yeetmeister II.txt'
games = []
wonGames = []
import resources as res


def updatestats():
    global games
    global wonGames
    files = os.listdir(res.userDirectory)
    files = [file for file in files if re.match(userFilePattern, file)]
    games = []
    wonGames = []
    for file in files:
        username = file[file.index("-") + 1:file.index(".")]
        userFileName = res.userDirectory + file
        with open(userFileName, "r") as userFile:
            userGames = [line.strip() for line in userFile.readlines()]
        games += [[username,
                   int(game[:game.index(" ")-1]),
                   game[game.index(" ")-1],
                   game[game.index("[")+1:game.index("]")]]
                  for game in userGames]

        wonGames += [[username,
                      int(game[:game.index(" ")-1]),
                      game[game.index("[")+1:game.index("]")]]
                     for game in userGames if game[game.index(" ")-1] == "W"]


def formatgame(game):
    msg = game[0] + ": " + {"W": "Won", "L": "Lost"}[game[2]] + " with " + str(game[1]) + " points"
    msg += " on " + game[3][:game[3].index(" ")] + " at " + game[3][game[3].index(" ")+1:]
    return msg


def playerstats():
    global games
    updatestats()
    username = res.validentry(res.getusernames(), "desired username")
    playerGames = [game for game in games if game[0] == username]
    print("%d games were found for that user%s" % (len(playerGames), (":" if len(playerGames) > 0 else ".")))
    print("\n".join([formatgame(game) for game in playerGames])) if len(playerGames) > 0 else None


def leaderboard():
    global wonGames
    updatestats()
    scoredGames = sorted([[score, name, time] for name, score, time in wonGames])
    print("Total games played: %d" % len(wonGames))
    getAmount = 5
    getAmount = len(wonGames) if len(wonGames) < getAmount else getAmount
    print("Top wins:")
    for pick in range(getAmount):
        msg = "%d: %d points scored by %s on %s at %s"
        picked = (scoredGames[::-1])[pick]
        print(msg % (pick+1, picked[0], picked[1], picked[2][:picked[2].index(" ")], picked[2][picked[2].index(" ")+1:]))

