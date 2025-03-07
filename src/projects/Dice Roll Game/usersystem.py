import sqlite3
import re
import os
from difflib import SequenceMatcher
from datetime import datetime
from __main__ import *

loggedInA = None
loggedInB = None

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    db = conn.cursor()

userDirectory = r"C:\Users\joe\Google Drive\Misc\Master Python Project\Programming Projects\Dice Roll Game\Users\\"
# Raw string containing the directory where users' files are stored - these contain

badChars = ":$;&/\\'\""  # characters to be stripped from an inputted string; could cause issues when parsed by eval()

numberPattern = re.compile("[0-9]")  # Match numbers
capPattern = re.compile("[A-Z]")  # Match capital lettes
symbolPattern = re.compile("[!-/:-@[-`{-~]")  # Match usual ASCII symbols

passwordMsgList = ["Enter a valid password. It should contain:",
                   "- At least two numbers",
                   "- At least one capital letter",
                   "- At least one symbol",
                   "- At least 7 characters total"]

passwordConstraints = [["len(re.findall(numberPattern, %s)) >= 2", "Password should contain at least two numbers"],
                       ["len(re.findall(capPattern, %s)) >= 1", "Password should contain at least one capital letter"],
                       ["len(re.findall(symbolPattern, %s)) >= 1", "Password should contain at least one symbol"],
                       ["len(%s) >= 7", "Password should be at least 7 characters long"]]
# The constraints that control whether a password is valid, using '%s' to denote where the userinput will be inserted

pwdAttemptsAllowed = 3
validUsers = ["a", "b"]

userFilePattern = re.compile("[1-9]*-.*\.txt")  # matches '1-Lordfirespeed.txt' and '14-Yeetmeister II.txt'
games = []
wonGames = []


def gettimenow():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def getusernames():
    db.execute("SELECT username FROM Users")
    return [uname for tupleuname in db.fetchall() for uname in tupleuname]
    # Returns a list of usernames as strings


def getuser(known, value):
    db.execute("SELECT ID, username FROM Users WHERE " + known + "=?", (value,))
    return db.fetchone()


def getuserfile(known, value):
    return "-".join([str(c) for c in getuser(known, value)]) + ".txt"


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    # returns a decimal between 0 and 1 denoting how similar two strings are. Useful for 'Did You Mean: ' etc


def validinput(msg, constraints):  # used to create new values, such as new users
    # msg will be printed when the input is asked for.
    # msg can be supplied as a list containing lines to be printed separately.
    # Supply constraints as a list of tuples in format (constaintStr, constraintMsg).
    # constaintStr should contain a %s to format with userInput and then pass to eval().
    # constraintMsg will be printed to tell the user what they did wrong if their input does not conform.
    global badChars
    valid = [False]

    while not all(valid):
        if type(msg) == str:  # check whether the message is a str or a list
            userInput = input(msg + "\n> ")  # string: take input as normal
        else:
            print("\n".join(msg))  # list: print the list's lines separately
            userInput = input("> ")  # take input

        strippedString = userInput.translate(userInput.maketrans(badChars, " " * len(badChars)))
        # strip 'bad' characters from the line
        insertString = ("'" + strippedString + "'")
        # the string to be inserted into the eval() statements needs to have string identifiers

        # [print((con[0] % [insertString for i in range(con[0].count("%s"))])  if con[0].count("%s") > 1
        #        else con[0] % insertString)
        #         for con in constraints]
        # The above helps with testing as it prints the statements that are being evaluated to the screen

        valid = [eval(con[0] % [insertString for i in range(con[0].count("%s"))] if con[0].count("%s") > 1
                 else con[0] % insertString)
                 for con in constraints]
        # valid is a list of booleans - evaluated constraints with the user's input formatted in
        # the first line of this statement checks whether there are multiple '%s's in the string,
        # to supply enough of the user input to satisfy the % formatting

        if not all(valid):  # if all the constraints are not valid
            print("Invalid input. Does not conform to constraint:\n" + constraints[valid.index(False)][1])
            # Tell the user what they did wrong
        elif userInput != strippedString:  # if the user's input conforms, but characters were stripped
            print("Invalid input. Does not confoem to constraint:\nMust not contain illegal characters")
            # Tell the user they used illegal characters
        else:  # the user had valid input
            checkCorrect = input("Confirm: '%s' ? (enter 'n' for no, any for yes)\n> " % userInput)
            # double-check what the user entered was what they wanted
            valid.append("n" not in checkCorrect.lower())
            # append whether "n" was in the user's 'check' response; if "n" is in the response,
            # then False will be appended, and all(valid) will return False, meaning the while loop is iterated again

    return userInput


def validentry(listinst, desired):  # used for known data, such as logins
    lowerlist = [value.lower() for value in listinst]
    correct = False
    while not correct:
        userInput = input("Please enter your %s:\n> " % desired)

        if userInput in listinst:
            correct = True
        elif userInput.lower() in lowerlist:
            didYouMean = listinst[lowerlist.index(userInput.lower())]
            check = input("Did you mean '%s'? ('n' to deny; any to confirm)\n> " % didYouMean)
            correct = "n" not in check.lower()
            if correct:
                userInput = didYouMean
        else:
            for checkName in lowerlist:
                if similar(userInput, checkName) > 0.6:
                    didYouMean = listinst[lowerlist.index(checkName)]
                    check = input("Did you mean '%s'? ('n' to deny; any to confirm)\n> " % didYouMean)
                    correct = "n" not in check.lower()
                    if correct:
                        userInput = didYouMean
                        break

            if not correct:
                print("That %s wasn't found. Try again." % desired)
    return userInput


def selectuser(known, value):
    global loggedInA
    global loggedInB

    if not loggedInA:
        userChose = "a"
    elif not loggedInB:
        userChose = "b"
    else:
        chosen = False
        while not chosen:
            userChose = input("Log in as player A or B?\n> ").lower()
            if userChose not in validUsers:
                print("Invalid input.")
                chosen = False
            else:
                current = getuser("ID", loggedInA)[1] if userChose == "a" else getuser("ID", loggedInB)[1]
                check = input(
                    "If you continue to log in, you will log out user '%s'. Continue? ('n' for no)\n> " % current)
                chosen = "n" not in check.lower()

    if userChose == "a":
        print("Logging in as user A...")
        return ["loggedInA = %d" % (getuser(known, value)[0])]
    else:
        print("Logging in as user B...")
        return ["loggedInB = %d" % (getuser(known, value)[0])]


def createuser():  # creates a valid user from user input using res.validinput()
    try:
        print("Welcome to the user creation utility.\nTo leave at any point, press CRTL + C.")
        firstName = validinput("Enter your first name. ", [["%s.isalpha()", "Name should be alphabetical - no numbers or spaces"]]).title()
        lastName = validinput("Enter your last name. ", [["%s.isalpha()", "Name should be alphabetical - no numbers or spaces"]]).title()
        username = validinput("Enter a unique username. ", [["%s not in getusernames()", "Username should be unique"]])
        password = validinput(passwordMsgList, passwordConstraints)
        values = (firstName, lastName, username, password, gettimenow())
        db.execute("INSERT INTO Users VALUES (NULL, ?, ?, ?, ?, ?)", values)
        conn.commit()
        newfilename = userDirectory + getuserfile("username", username)
        with open(newfilename, "w"):  # create a new file with the name '[ID]-[Username].txt' in the Users directory
            pass
        print("User successfully created!")

        return selectuser("username", username)

    except KeyboardInterrupt:
        print("Leaving user creating utility...")


def login():
    global loggedInA
    global loggedInB
    global validUsers
    try:
        db.execute("SELECT * FROM Users")
        userList = db.fetchall()
        usernameList = [user[3] for user in userList]
        enteredUsername = validentry(usernameList, "username")
        print("Logging in as '%s'..." % enteredUsername)
        userIndex = usernameList.index(enteredUsername)
        correctPassword = userList[userIndex][4]
        for i in range(pwdAttemptsAllowed, 0, -1):
            userInput = input("Attempt #%d: Enter Password.\n> " % i)
            if userInput != correctPassword:
                print("Password incorrect. %d Attempts remaining." % (i-1))
                if i-1 == 0:
                    print("Failed login.")
                    return None
            else:
                print("Welcome, %s %s." % (userList[userIndex][1], userList[userIndex][2]))
                break

        return selectuser("username", enteredUsername)
        
    except KeyboardInterrupt:
        print("Cancelling login...")
        return None


def updatestats():
    global games
    global wonGames
    files = os.listdir(userDirectory)
    files = [file for file in files if re.match(userFilePattern, file)]
    games = []
    wonGames = []
    for file in files:
        username = file[file.index("-") + 1:file.index(".")]
        userFileName = userDirectory + file
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
    username = validentry(getusernames(), "desired username")
    playerGames = [game for game in games if game[0] == username]
    print("%d games were found for that user%s" % (len(playerGames), (":" if len(playerGames) > 0 else ".")))
    print("\n".join([formatgame(game) for game in playerGames[::-1]])) if len(playerGames) > 0 else None


def leaderboard():
    global wonGames
    updatestats()
    scoredGames = sorted([[score, name, time] for name, score, time in wonGames])
    print("Total games played: %d" % len(wonGames))
    getAmount = 5
    getAmount = len(wonGames) if len(wonGames) < getAmount else getAmount
    if getAmount == 0:
        print("No games played!")
    else:
        print("Top wins:")
        for pick in range(getAmount):
            msg = "%d: %d points scored by %s on %s at %s"
            picked = (scoredGames[::-1])[pick]
            print(msg % (pick+1, picked[0], picked[1], picked[2][:picked[2].index(" ")], picked[2][picked[2].index(" ")+1:]))


def getusers():
    db.execute("SELECT * FROM Users")
    return db.fetchall()


def printusers():
    userlist = getusers()
    [print(", ".join([str(c) for c in user])) for user in userlist]


def delusers(IDs):
    global userDirectory
    # Delete users with IDs
    intIDs = [IDn[0] if type(IDn) == tuple else IDn for IDn in IDs]
    tupIDs = [(IDn,) if type(IDn) == int else IDn for IDn in IDs]

    for ID in intIDs:
        userFilePath = userDirectory + getuserfile("ID", ID)
        try:
            os.remove(userFilePath)
        except FileNotFoundError:
            pass

    db.executemany("DELETE FROM Users WHERE ID=?", tupIDs)
    conn.commit()
    # Retrieve user IDs in use
    InUseIDs = [user[0] for user in getusers()]
    InUseIDs.append(0)
    InUseIDs = [(IDn,) if type(IDn) == int else IDn for IDn in InUseIDs]
    # Update the database metadata with the maximum in use ID in the table, to prevent large gaps between IDs
    db.execute("UPDATE sqlite_sequence SET seq = ? WHERE name='Users'", max(InUseIDs))
    conn.commit()


db.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = db.fetchall()
tables = [table for tabletuple in tables for table in tabletuple]


if "Users" not in tables:
    db.execute('''CREATE TABLE Users
              (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
               firstname text,    
               lastname text, 
               username text UNIQUE, 
               password text, 
               creationtimestr text)''')
    tables.append("Users")
