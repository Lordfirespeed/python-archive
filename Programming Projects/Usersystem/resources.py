import sqlite3
import re
from __main__ import *
# import all variables from whatever is importing the file
from difflib import SequenceMatcher
from datetime import datetime

conn = sqlite3.connect("database.db")
db = conn.cursor()

userDirectory = r"C:\Users\joe\Google Drive\Misc\Master Python Project\Programming Projects\Dice Roll Game\Users\\"
# Raw string containing the directory where users' files are stored - these contain

badChars = ":$;&/\\'\""  # characters to be stripped from an inputted string; could cause issues when parsed by eval()


def gettimenow():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def getusernames():
    db.execute("SELECT username FROM Users")
    return [uname for tupleuname in db.fetchall() for uname in tupleuname]
    # Returns a list of usernames as strings - should only be called from other files that have opened the database


def getuserfile(known, value):
    db.execute("SELECT ID, username FROM Users WHERE " + known + "=?", (value,))
    return "-".join([str(c) for c in db.fetchone()]) + ".txt"


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
