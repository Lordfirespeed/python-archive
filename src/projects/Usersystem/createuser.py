import sqlite3
import re
from __main__ import *

conn = sqlite3.connect("database.db")
db = conn.cursor()

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


import resources as res  # imports python file 'resources.py', which includes the validinput() function


def createuser():  # creates a valid user from user input using res.validinput()
    try:
        print("Welcome to the user creation utility.\nTo leave at any point, press CRTL + C.")
        firstName = res.validinput("Enter your first name. ", [["%s.isalpha()", "Name should be alphabetical - no numbers or spaces"]]).title()
        lastName = res.validinput("Enter your last name. ", [["%s.isalpha()", "Name should be alphabetical - no numbers or spaces"]]).title()
        username = res.validinput("Enter a unique username. ", [["%s not in getusernames()", "Username should be unique"]])
        password = res.validinput(passwordMsgList, passwordConstraints)
        values = (firstName, lastName, username, password, res.gettimenow())
        db.execute("INSERT INTO Users VALUES (NULL, ?, ?, ?, ?, ?)", values)
        conn.commit()
        newfilename = res.userDirectory + res.getuserfile("username", username)
        with open(newfilename, "w"):  # create a new file with the name '[ID]-[Username].txt' in the Users directory
            pass
        print("User successfully created!")

    except KeyboardInterrupt:
        print("Leaving user creating utility...")

