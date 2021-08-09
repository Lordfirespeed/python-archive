import sqlite3
import random

loggedInA = 1
loggedInB = 2

conn = sqlite3.connect("database.db")
db = conn.cursor()

import usersystem

# Initialise colours and numbers; Order denotes rank; Red beats black, black beats yellow, yellow beats... and so on
# If there are more colours, the amount a colour can beat is n // 2 (where n == num of cards)
# e.g with ["Red", "Black", "Yellow", "Purple", "Blue"]
# Red beats black and yellow, black beats yellow + purple... blue beats red and black.
colours = ["Red", "Black", "Yellow"]  # must be an odd number of colours
canBeat = int(len(colours) / 2)
numberofCards = 10
numbers = range(1, numberofCards + 1)


def getdeck():
    global colours
    global numbers
    # Returns a list of dictionaries (cards)
    return [{"colour": colour, "value": number} for colour in colours for number in numbers]


def shuffle(cards):
    # Create a new list, so as not to affect the old one (just in case)
    currentCards = list(cards)
    shuffled = []
    # Pick random indexes from currentCards and add that card to the end of shuffled. Delete the card from currentCards
    for i in range(len(cards)):
        index = random.randrange(len(currentCards))
        shuffled.append(currentCards[index])
        del currentCards[index]
    # Return the shuffled deck
    return shuffled


def gameround(cards, players=["Player A", "Player B"]):
    global colours
    global canBeat
    # Player A's draw
    input("%s's Draw..." % players[0])
    playerACard = cards.pop()
    print("You drew %s %s." % tuple(playerACard.values()))
    # Player B's draw
    input("%s's Draw..." % players[1])
    playerBCard = cards.pop()
    print("You drew %s %s." % tuple(playerBCard.values()))

    # If the players both have the same card colour
    if playerACard["colour"] == playerBCard["colour"]:
        # Return the player who had the higher valued card and the two cards they won
        return ["PlayerA", [playerACard, playerBCard]] if playerACard["value"] > playerBCard["value"] else ["PlayerB", [playerACard, playerBCard]]
    else:  # Otherwise the players have different colours
        playerSet = {playerACard["colour"], playerBCard["colour"]}
        for i in range(len(colours)):
            # Check the sets of colours in colours until the pair matches the pair that the players
            for checki in range(i+1, i+canBeat+1):
                cardsSet = {colours[i], (colours*2)[checki]}
                #print(cardsSet)
                if playerSet == cardsSet:
                    winningColour = colours[i]
                    # Return the player with the winning coloured card and the two cards they won
                    return ["PlayerA", [playerACard, playerBCard]] if playerACard["colour"] == winningColour else ["PlayerB", [playerACard, playerBCard]]


def playgame():
    # Pull in the two logged in users from global scope
    global loggedInA
    global loggedInB

    # If both/either users are not logged in, tell the user(s) what needs to be done
    if (not loggedInA) and (not loggedInB):
        print("No users are logged in. Two people need to log in to play.")
        return None
    elif not loggedInA:
        print("User A is not logged in. Two people need to be logged in to play.")
        return None
    elif not loggedInB:
        print("User B is not logged in. Two people need to be logged in to play.")
        return None

    # Grab the usernames of the two players based on ID
    usernameA = usersystem.getuser("ID", loggedInA)[1]
    usernameB = usersystem.getuser("ID", loggedInB)[1]
    playerNames = [usernameA, usernameB]
    # Assign a blank hand to A and B
    cardsA, cardsB = [], []
    # Create a shuffled card deck
    cardDeck = shuffle(getdeck())

    while len(cardDeck) > 0:  # While there are still cards in the deck
        # Use the gameround() function to find who won, and what cards they won
        playerWon, cardsWon = gameround(cardDeck, playerNames)
        if playerWon == "PlayerA":  # if Player A won
            print("%s won that round." % usernameA)  # Tell them
            cardsA += cardsWon  # Add their cards to their hand
        else:  # Otherwise, Player B won
            print("%s won that round." % usernameB)  # Tell them
            cardsB += cardsWon  # Add their cards to their hand
        # Tell them how many cards are left in the deck
        print("There are %s cards left in the deck.\n" % (len(cardDeck) if len(cardDeck) > 0 else "no"))

    # Give Player A and B a 'score' based on their cards - easier to compare
    scoreA, scoreB = len(cardsA), len(cardsB)

    # Get the username of the winner
    winner = usernameA if scoreA >= scoreB else usernameB
    # Get the username of the loser
    loser = (set(playerNames) - {winner}).pop()

    # Game over message
    print("GAME OVER!")
    print("%s won with a total of %d cards." % (winner, max([scoreA, scoreB])))
    print("They had: " + ", ".join([" ".join([str(c) for c in card.values()]) for card in cardsA]))
    print("%s lost, with only %d cards. Oh dear!" % (loser, min([scoreA, scoreB])))

    # Retrieve the winner and loser filepaths
    winnerFileName = usersystem.userDirectory + usersystem.getuserfile("username", winner)
    loserFileName = usersystem.userDirectory + usersystem.getuserfile("username", loser)

    # Append the score, 'W' (win) and time of the game to winner's file
    with open(winnerFileName, "a") as winnerFile:
        winnerFile.write(str(max([scoreA, scoreB])) + "W [" + usersystem.gettimenow() + "]\n")

    # Append the score, 'L' (loss) and time of the game to loser's file
    with open(loserFileName, "a") as loserFile:
        loserFile.write(str(min([scoreA, scoreB])) + "L [" + usersystem.gettimenow() + "]\n")


def gethelp():
    global validCommands
    # Print a '-' bulleted list of valid commands
    print("Valid commands:\n- " + "\n- ".join(validCommands))


def exitgame():
    # Exit the game gracefully
    print("Thank you for testing Joe's Card Game.")
    exit(0)


# Valid commands the user can use, followed by their prefix/module
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
    try:
        usersystem.loggedInA = loggedInA
        usersystem.loggedInB = loggedInB
        userinput = usersystem.validentry(list(validCommands), "command")
        exec("execCommands = " + validCommands[userinput] + userinput + "()", globals(), locals())
        if execCommands:
            [exec(cmd, globals()) for cmd in execCommands]
            execCommands = None
    except KeyboardInterrupt:
        pass
